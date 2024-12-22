from rest_framework import serializers
from accounts.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail":"password doesn't match"})
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
