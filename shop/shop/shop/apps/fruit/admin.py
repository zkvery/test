from django.contrib import admin

# Register your models here.
from django.contrib import admin
from fruit.models import  TypeInfo,GoodInfo,Banner,CartInfo

# Register your models here.
admin.site.register(TypeInfo)
admin.site.register(GoodInfo)
admin.site.register(Banner)
admin.site.register(CartInfo)

