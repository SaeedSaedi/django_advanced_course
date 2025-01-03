from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ActivationResendApiSerializer,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from accounts.models import Profile

# from django.core.mail import send_mail
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

User = get_user_model()


class RegistrationApiView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email = EmailMessage(
                "email/active.tpl", {"token": token}, "saeed@saeed.com", to=[email]
            )
            EmailThread(email).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class CustomDiscardAuthToken(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user

        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": "wrong password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ActivationEmailView(APIView):

    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
            user_id = token.get("user_id")

        except ExpiredSignatureError:
            Response({"details": "Expired"})
        except InvalidSignatureError:
            Response({"details": "invalid"})
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({"details": "your account was activated before"})
        else:
            user_obj.is_verified = True
            user_obj.save()
            return Response({"details": "your account activated"})


class ActivationResendEmailView(generics.GenericAPIView):

    serializer_class = ActivationResendApiSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivationResendApiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user_obj)
        email = EmailMessage(
            "email/active.tpl",
            {"token": token},
            "saeed@saeed.com",
            to=[user_obj.email],
        )
        EmailThread(email).start()
        return Response("email sent", status=status.HTTP_201_CREATED)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# class TestEmailSend(generics.GenericAPIView):

#     def post(self, request, *args, **kwargs):

#         self.email = "saeed@saeed.com"
#         user_obj = get_object_or_404(User, email=self.email)
#         token = self.get_tokens_for_user(user_obj)

#         # send_mail(
#         #     "Subject here",
#         #     "Here is the message.",
#         #     "from@example.com",
#         #     ["to@example.com"],
#         #     fail_silently=False,
#         # )
#         # send_mail("email/hello.tpl", {"name": "ali"}, "saeed@saeed.com", ["hi@hi.com"])

#         email = EmailMessage(
#             "email/hello.tpl", {"token": token}, "saeed@saeed.com", ["hi@hi.com"]
#         )
#         EmailThread(email).start()
#         return Response("email sent")

#     def get_tokens_for_user(self, user):

#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)
