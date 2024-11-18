from rest_framework import serializers
from extras.models import Address, Extras


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = "__all__"
