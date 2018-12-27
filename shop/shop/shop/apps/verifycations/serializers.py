from django_redis import get_redis_connection
from rest_framework import serializers
class CheckImageCodeSerializer(serializers.Serializer):
    image_code_id = serializers.UUIDField()
    text = serializers.CharField(max_length=4,min_length=4)

    def validate(self, attrs):
        text = attrs['text']
        print('用户输入的验证码%s'%text)
        image_code_id = attrs['image_code_id']
        print('id%s'%image_code_id)
        redis_conn = get_redis_connection('verify_codes')
        real_image_code = redis_conn.get('img_%s'%image_code_id)

        if real_image_code is None:
            print('图片验证码过期')
            raise serializers.ValidationError('无效的图片验证码')
        return attrs



