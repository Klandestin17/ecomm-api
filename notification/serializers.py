from rest_framework import serializers
from notification import models


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
