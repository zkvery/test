# 自定义函数，在settings中需要配置JWT_RESPONSE_PAYLOAD_HANDLER属性
def response_payload_handler(token, user=None, request=None):
    '''自定义认证成功返回数据'''
    return {
        'token': token,
        'user_id': user.id,
        'user_name': user.username
    }


def get_user_by_count(account):
    try:
        if re.match(r'1[3-9]\d{9}', account):
            user = User.objects.filter(mobile=account).first()
        else:
            user = User.objects.filter(username=account).first()

    except Exception as e:
        return None

    return user


import re
from .models import User


from django.contrib.auth.backends import ModelBackend


#  登录用户名或者手机号都可以认证成功
class UsernameMobileAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_count(username)
        if user is not None and user.check_password(password):
            return user










