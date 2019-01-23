from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# Create your views here.
from users.models import User
from users.serializers import CreateUserSerializer, ReturnUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class UsernameCountView(APIView):
    """
    用户名数量
    """
    def get(self, request, username):
        """
        获取指定用户名数量
        """
        count = User.objects.filter(username=username).count()
        # 把结果查出来 让前端自己去判断吧，1存在 0不存在
        data = {
            'username': username,
            'count': count
        }

        return Response(data)

class MobileCountView(APIView):
    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()

        data = {
            'mobile': mobile,
            'count': count
        }
        return Response(data)

from rest_framework.permissions import IsAuthenticated
class ReturnUser(RetrieveAPIView):

    serializer_class = ReturnUserSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        print('user============%s' % self.request.user)
        return self.request.user
