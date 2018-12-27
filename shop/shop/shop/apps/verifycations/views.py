from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from shop.shop.libs.captcha.captcha import captcha
from shop.shop.utils import constants
from django_redis import get_redis_connection
from rest_framework.views import APIView

from verifycations.serializers import CheckImageCodeSerializer


class ImageCodeView(APIView):
    def get(self,request,image_code_id):
        text,image=captcha.generate_captcha()
        redis_conn = get_redis_connection('verify_codes')
        redis_conn.setex('img_%s' %image_code_id,constants.IMAGE_CODE_REDIS_EXPRIES,text)
        return HttpResponse(image,content_type='image/jpg')

import random
from rest_framework.generics import GenericAPIView
from shop.celery_tasks.sms_code.tasks import send_sms_code
from rest_framework.response import Response
class SmsCodeView(GenericAPIView):
    serializer_class = CheckImageCodeSerializer
    def get(self,request,mobile):
        print('mobile=======%s,data========%s' % (mobile, request.query_params))
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        sms_code = '%06d' %random.randint(0,999999)
        print('sms_code=========%s'%sms_code)
        redis_conn = get_redis_connection('verify_codes')
        redis_conn.setex('sms_%s'%mobile,constants.SMS_CODE_REDIS_EXPRIES,sms_code)
        send_sms_code.delay(mobile,sms_code)
        return Response({'message':'ok'})
