from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# MyCustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# my custom jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ResendActivationSerializer,
)
from ...models import Profile

# email modules
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken

# import user from auth modelof project that set in settings
from django.contrib.auth import get_user_model

User = get_user_model()

# activation and resend activation class
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data={
    #             'email':serializer.validated_data['email']
    #         }
    #     return Response(data,status=201)

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        # serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            validated_email = serializer.validated_data["email"]

            user_obj = get_object_or_404(User, email=validated_email)
            activate_token_link = self.get_tokens_for_user(user_obj)

            email_obj = EmailMessage(
                "email/registeration.tpl",
                {"user_name": user_obj, "token": activate_token_link},
                "from@gmail.com",
                to=[validated_email],
            )
            EmailThread(email_obj).start()

            data = {
                "email": validated_email,
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationAPIView(APIView):
    # def get(self,request,token,*args,**kwargs):
    #     data={
    #         'token':jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256']),
    #         'kwargs':kwargs,
    #         'args':args,
    #     }
    #     return Response(data)

    def get(self, request, token, *args, **kwargs):
        # decode->user_id
        try:
            token = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"]
            )
            # if token valid
            user_id = token.get("user_id")
            # object user
            user_obj = User.objects.get(pk=user_id)
            # is_verified ==True
            if user_obj.is_verified:
                return Response(
                    {"details": "your account has already been verified!!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user_obj.is_verified = True
            user_obj.save()

        # if token not valid -> error
        except ExpiredSignatureError:
            return Response(
                {"details": "sorry!! token has been expired "},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except InvalidSignatureError:
            return Response(
                {"details": "sorry token has not valid!!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "details": "your account has been verified and activated succussfully"
            },
            status=status.HTTP_200_OK,
        )


class ResendActivationAPIView(generics.GenericAPIView):
    serializer_class = ResendActivationSerializer

    def post(self, request, *args, **kwargs):
        # email=request.data.get('email')

        # serializer=self.serializer_class(data=request.data)
        serializer = ResendActivationSerializer(data=request.data)

        # if serializer.is_valid():

        #     # user_obj=get_object_or_404(User,email=self.email)
        #     user_obj=serializer.validated_data['user']
        #     activate_token_link=self.get_tokens_for_user(user_obj)

        #     email_obj= EmailMessage('email/registeration.tpl', {'user_name':'request.user.username','token':activate_token_link }, 'from@gmail.com', to=[user_obj.email])
        #     EmailThread(email_obj).start()

        #     return Response({'detail':'email sent'},status=status.HTTP_200_OK)

        # else:
        #     return Response({'detail':'request failed!!'},status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        activate_token_link = self.get_tokens_for_user(user_obj)

        email_obj = EmailMessage(
            "email/registeration.tpl",
            {
                "user_name": "request.user.username",
                "token": activate_token_link,
            },
            "from@gmail.com",
            to=[user_obj.email],
        )
        EmailThread(email_obj).start()

        return Response({"detail": "email sent"}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class MyCustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )


class CustomDestroyAuthToken(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.UpdateAPIView):
    """
    this class is for changing password with api and if we want to use patch with put method,
    must user UpdateView not GenericAPIView and change put method to update
    """

    model = User
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # check old pass
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed succussfully "},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    this class need lookupfield in APIView but we dont want to use user_id.so we override get_queryset or get_object()
    to find profile of user to prfoile detail page
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # lookup_field='pk'

    # def get_object(self):
    #     return super().get_object()

    # def get_queryset(self):
    #     return super().get_queryset()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


# class TestEmailSend(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):
#         send_mail(
#             'subject here',
#             'here is the message',
#             'from@example.com',
#             ['to@example.com'],
#             fail_silently=False,
#         )
#         return Response('email sent')


# from mail_templated import send_mail
# class TestEmailSend(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):

#         send_mail('email/hello.tpl', {'user_name':'request.user.username' }, 'from@gmail.com', ['bahmanpn@gmail.com'])

#         return Response('email sent')


# changed email class to email message to more control messages and use threding
class TestEmailSend(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        # static email is going to change dynamic in registration class
        self.email = "bahmanpn@gmail.com"
        user_obj = get_object_or_404(User, email=self.email)
        activate_token_link = self.get_tokens_for_user(user_obj)

        email_obj = EmailMessage(
            "email/hello.tpl",
            {
                "user_name": "request.user.username",
                "token": activate_token_link,
            },
            "from@gmail.com",
            to=[self.email],
        )
        EmailThread(email_obj).start()

        return Response("email sent")

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
