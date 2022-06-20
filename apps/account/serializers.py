
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .

User = get_user_model()

# class RegistrationSerializer(serializers.Serializer):
#     nickname = serializers.CharField(max_length=20)

class RegistrationSerializer(serializers.Serializer):
    password_confirm = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('nickname', 'phone', 'password')

    def validate_nickname(self, nickname):
        if User.objects.filter(nickname=nickname).exists():
            raise serializers.ValidationError('This nickname is already taken. Please choose another one')
        return nickname

    def validate_phone(self, phone):
        phone = normalize_phone()
        if len(phone) != 13:
            raise serializers.ValidationError('Invalid phone format')

        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('Phone is already exists')
        return phone

    def validate(self, attrs: dict):
        print(attrs)
        password1 = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if not any(i for i in password1 if i.isdigit()):
            raise serializers.ValidationError('Password must contain at least one digit')

        if password1 != password_confirm:
            raise serializers.ValidationError('Password do not match')
