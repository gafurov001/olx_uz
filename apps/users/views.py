from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from jsonschema._format import is_email
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import UserModelSerializer, UserLoginSerializer


@extend_schema(tags=['user'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# @extend_schema(tags=['user'])
# class UserUpdatePasswordUpdateAPIView(UpdateAPIView):

# @extend_schema(tags=['user'])
# class ChangePasswordUserGenericAPIView(UpdateAPIView):
#     queryset = User
#     serializer_class = ChangePasswordUserModelSerializer
#
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj
#
#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             if not self.object.chek_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#         self.object.set_password(serializer.data.get("new_password"))
#         self.object.save()
#
#
# @extend_schema(tags='user')
# class LoginUserAPIView(APIView):
#     permission_classes = AllowAny,
#     authentication_classes = SessionAuthentication,
#
#     def post(self, request):
#         data = request.data
#         assert validate_email(data)
#         assert validate_password(data)
#         serializer = UserLoginModelSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.check_user(data)
#             login(request, user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
@extend_schema(tags=['user'])
class LoginAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = AllowAny,

    def post(self, request):
        if not is_email(request.data['email_or_phone_number']):
            user = authenticate(request=request, username=request.data['email_or_phone_number'],
                                password=request.data['password'])
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token), "refresh": str(refresh)})
        # else:
        #     user = User.objects.filter(phone_number=request.data['email_or_phone_number'], password=request.data['password'])
        # return user
