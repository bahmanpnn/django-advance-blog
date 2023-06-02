from django.urls import path
from .views import *
# from rest_framework.authtoken.views import ObtainAuthToken

app_name='api-v1'

urlpatterns = [
    #registration
    path('registration/',RegistrationAPIView.as_view(),name='registration-api'),
    # path('token/login/', ObtainAuthToken.as_view(),name='token-login'),
    
    #change password
    #reset password
    
    #login token
    path('token/login/', MyCustomAuthToken.as_view(),name='custom-token-login'),
    # path('api-token-auth/', views.obtain_auth_token)

    # logout(destroy) token
    path('token/logout/',CustomDestroyAuthToken.as_view(),name='custom-token-logout')

    #login jwt
]