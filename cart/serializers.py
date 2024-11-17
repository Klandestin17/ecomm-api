from rest_framework import serializers
from cart import models
from core.serializers import ProductSerializers


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializers(read_only=True)

    class Meta:
        model = models.Cart
        exclude = ["userId", "created_at", "updated_at"]
