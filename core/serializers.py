from rest_framework import serializers
from . import models


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('title', 'id', 'imageUrl')


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ('title', 'id', 'imageUrl')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
