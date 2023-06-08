from django.urls import path
from ..views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    #registration
    path('registration/',RegistrationAPIView.as_view(),name='registration-api'),
    # path('token/login/', ObtainAuthToken.as_view(),name='token-login'),
    
    #test email
    path('test-email/',TestEmailSend.as_view(),name='test-email'),

    #activation
    # path('activate/confirm/',,name=''),

    #resend activation
    # path('activate/resend/',,name=''),

    #change password
    path('change_password/',ChangePasswordAPIView.as_view(),name='change-password'),
    
    #reset password
    
    #login token
    path('token/login/', MyCustomAuthToken.as_view(),name='custom-token-login'),
    # path('api-token-auth/', views.obtain_auth_token)

    # logout(destroy) token
    path('token/logout/',CustomDestroyAuthToken.as_view(),name='custom-token-logout'),

    #login jwt
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #custom jwt
    path('jwt/custom/create/',CustomTokenObtainPairView.as_view(), name='custom-token_obtain_pair'),
    
]

# docker-compose exec backend sh -c "pip install django==4.0 djangorestframework==3.13"