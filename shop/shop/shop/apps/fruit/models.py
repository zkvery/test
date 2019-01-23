from django.db import models

# Create your models here.

# 商品分类的模型类
class TypeInfo(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='type')
    class_name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# 商品表
class GoodInfo(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(TypeInfo,on_delete=models.CASCADE,related_name='subs')
    # 商品图片
    image = models.ImageField(upload_to='good')
    # 简介
    jianjie = models.CharField(max_length=200)
    # 价钱
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # 单位
    unit = models.CharField(max_length=30)
    # 人气，点击量 浏览量
    click = models.IntegerField(default=0)
    istop = models.BooleanField(default=True)  # 是否推荐
    def __str__(self):
        return self.name

# 轮播图
class Banner(models.Model):
    image = models.ImageField(upload_to='banner')

# 购物车
class CartInfo(models.Model):
    good = models.ForeignKey(GoodInfo,on_delete=models.CASCADE)
    num = models.IntegerField()
    sum_price = models.DecimalField(max_digits=5,decimal_places=2)