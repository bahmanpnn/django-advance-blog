from django.urls import path, include
from .views import *

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    # v2
    path("api/v2/", include("djoser.urls")),
    # add jwt urls from djoser
    path("api/v2/", include("djoser.urls.jwt")),
]
