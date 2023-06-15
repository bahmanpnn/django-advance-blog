from django.urls import path
from .. import views

# from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    # user profile
    path("", views.ProfileAPIView.as_view(), name="profile"),
    # path('<int:pk>/',ProfileAPIView.as_view(),name='profile'), ==>for lookup_field='pk'
]
