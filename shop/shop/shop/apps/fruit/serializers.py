from rest_framework import serializers

from fruit.models import TypeInfo, GoodInfo, Banner


class GoodeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodInfo
        fields = ('id','name','image','price','istop')

class ReturnTypeerializer(serializers.ModelSerializer):
    subs = GoodeInfoSerializer(many=True, read_only=True)
    class Meta:
        model = TypeInfo
        fields = '__all__'

class ReturnBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class GoodDetailSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name')
    class Meta:
        model = GoodInfo
        fields = ('id','name','image','jianjie','price','unit','type')

class AllTypeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = TypeInfo
        exclude = ('image',)

class GoodListSerilaizer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name')
    class Meta:
        model = GoodInfo
        fields = ('id','name','intro','image','price','unit','content','type')
