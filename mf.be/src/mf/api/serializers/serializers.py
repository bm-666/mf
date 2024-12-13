from rest_framework import serializers
from ..models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'stock', 'category')

class ProductListSerializer(serializers.ListSerializer):
    ...
class PartnerTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerTask
        fields = ("id", "name", "url", "reward")