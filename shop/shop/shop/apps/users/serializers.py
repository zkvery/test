from rest_framework import serializers
import re

from rest_framework_jwt.settings import api_settings

from users.models import User
from django_redis import get_redis_connection

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='确认密码',required=True,allow_null=False,allow_blank=False,write_only=True)
    sms_code = serializers.CharField(label='短信验证码',required=True,allow_null=False,allow_blank=False,write_only=True)
    allow = serializers.BooleanField(label='同意协议',required=True,write_only=True)
    token = serializers.CharField(label='登录状态token', read_only=True)  # 增加token字段

    class Meta:
        model = User
        fields = ('id','username','password','password2','sms_code','mobile','allow','token')

        extra_kwargs = {
            'id' :{'read_only':True},
            'username':{
                'min_length':5,
                'max_length':20,
                'error_messages':{
                    'min_length':'仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名'
                }
            },
            'password':{
                'write_only':True,
                'min_length': 8,
                'max_length': 20,
                'error_messages':{
                    'min_length':'仅允许8-20个字符的密码',
                    'max_length':'仅允许8-20个字符的密码',
                }
            }
        }

    def validate_mobile(self, mobile):
        if not re.match(r'1[3-9]\d{9}',mobile):
            return serializers.ValidationError('手机号不正确')
        return mobile

    def validate_allow(self, allow):
        if allow == False:
            return serializers.ValidationError('请勾选同意')
        return allow


    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']

        if password != password2:
            return serializers.ValidationError('两次密码不一致')

        redis_conn = get_redis_connection('verify_codes')
        mobile = attrs['mobile']
        sms_code = redis_conn.get('sms_%s'%mobile)
        if sms_code is None:
            return serializers.ValidationError('无效的短信验证码')

        if attrs['sms_code'] != sms_code.decode():
            raise serializers.ValidationError('短信验证码错误')

        return attrs

    def create(self, validated_data):
        #  移除数据库中不存在的字段
        del validated_data['password2']
        del validated_data['allow']
        del validated_data['sms_code']

        user = super(CreateUserSerializer, self).create(validated_data)
        # 使用django自带的认证密码加密
        user.set_password(validated_data['password'])

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 将token保存到user对象中，随着返回值返回给前端
        user.token = token
        print('保存token')
        user.save()
        return user

class ReturnUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','mobile','username','password')


