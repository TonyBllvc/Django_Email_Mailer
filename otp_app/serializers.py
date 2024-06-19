from rest_framework import serializers
from .models import OtpToken

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpToken
        fields = '__all__'