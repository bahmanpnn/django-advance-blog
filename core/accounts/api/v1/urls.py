from django.urls import path
from .views import *

app_name='api-v1'

urlpatterns = [
    #registration
    path('registration/',RegistrationAPIView.as_view(),name='registration-api'),
    #change password
    #reset password
    #login token
    #login jwt
]