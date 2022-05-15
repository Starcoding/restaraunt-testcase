from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("api/v1/foods/", include(("api.urls", "api"), namespace="v1")),
]
