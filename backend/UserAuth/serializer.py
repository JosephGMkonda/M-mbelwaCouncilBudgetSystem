from django.contrib.models import User
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id','username']