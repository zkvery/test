from django.shortcuts import render

# Create your views here.
from fruit.models import TypeInfo, Banner, GoodInfo
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .serializers import ReturnTypeerializer, ReturnBannerSerializer, GoodDetailSerializer, GoodeInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class GetTypeInfo(APIView):
    def get(self,request):
        goods = TypeInfo.objects.all()
        print('goods==========%s'%goods)
        ser = ReturnTypeerializer(instance=goods,many=True)
        ser = ser.data
        print('ser==========%s'%ser)
        return Response(ser)

class GetBannerInfo(APIView):
    def get(self,request):
        banner = Banner.objects.all()
        print('banner==========%s'%banner)
        ser = ReturnBannerSerializer(instance=banner,many=True)
        ser = ser.data
        print('bannerser==========%s'%ser)
        return Response(ser)

class GoodDetail(RetrieveAPIView):
    serializer_class = GoodDetailSerializer
    def get_queryset(self):
        good = GoodInfo.objects.get(id=self.kwargs['pk'])
        print('good========%s'%good)
        print('kwargs%s' % self.kwargs['pk'])
        print('kwargs2%s' % self.kwargs.get('pk'))
        good.click +=1
        good.save()
        return GoodInfo.objects.filter(id=self.kwargs.get('pk'))


from .serializers import GoodListSerilaizer
from .models import GoodInfo
from rest_framework.pagination import PageNumberPagination
class GoodInforPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 2
    max_page_size = 5

class GoodsOrderingView(APIView):
    def get(self,request,pk):
        type_good = TypeInfo.objects.get(pk=pk)
        ser = ReturnTypeerializer(type_good)
        return Response(ser.data,status=200)










