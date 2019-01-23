from django.conf.urls import url

from fruit import views

urlpatterns = [

    url(r'^typeinfo/$', views.GetTypeInfo.as_view()),
    url(r'^get_banner/$', views.GetBannerInfo.as_view()),
    url(r'^gooddetail/(?P<pk>\d+)/$', views.GoodDetail.as_view()),
    url(r'^goodlists/(?P<pk>\d+)/$',views.GoodsOrderingView.as_view()),

]