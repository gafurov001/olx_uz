from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(Serializer):
    email_or_phone_number = CharField(required=True)
    password = CharField(required=True)

    def validate(self, attrs):
        return super().validate(attrs)


class ChangePasswordUserModelSerializer(ModelSerializer):
    user = CharField()
    new_password = CharField(required=True)
    old_password = CharField(required=True)

    class Meta:
        model = User
        fields = 'new_password', 'old_password', 'user'

# class UserLoginModelSerializer(ModelSerializer):
#     phone_number = EmailField()
#     password = CharField()
#
#     def check_user(self, clean_data):
#         user = authenticate(phone_number=clean_data['phone_number'], password=clean_data['password'])
#         if not user:
#             raise ValidationError('user nor found')
#         return user
