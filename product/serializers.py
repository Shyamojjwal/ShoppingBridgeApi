from rest_framework import serializers;
from common.models import *


class ProductLIstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'price', 'description', 'created_date', 'updated_date')


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True,
        max_length=200,
        error_messages={'blank': "Title can't be blank"},
        label='Title'
    )
    brand = serializers.CharField(
        required=True,
        max_length=200,
        error_messages={'blank': "Title can't be blank"},
        label='Brand'
    )
    price = serializers.CharField(
        required=True,
        max_length=50,
        error_messages={'blank': "Title can't be blank"},
        label='Price'
    )
    description = serializers.CharField(
        required=True,
        error_messages={'blank': "Description can't be blank"},
        label='Description'
    )

    class Meta:
        model = Product
        fields = ('title', 'brand', 'price', 'description')
