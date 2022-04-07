from rest_framework import serializers
from .models import Product, TestModel


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=250)
    slug = serializers.SlugField(max_length=120)
    price = serializers.CharField(max_length=30)
    discount_price = serializers.CharField(max_length=30)
    image = serializers.ImageField()
    is_published = serializers.BooleanField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
