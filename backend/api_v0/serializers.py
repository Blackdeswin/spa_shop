from rest_framework import serializers
from products.models import Products


class ProductsPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'price',
            'image',
            'category',
        ]


class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'price',
        ]
