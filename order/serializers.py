from rest_framework import serializers
from order import models


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
