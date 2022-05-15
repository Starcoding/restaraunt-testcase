from django.urls import path, include
from rest_framework.routers import re_path
from .views import FoodApi


urlpatterns = [
    re_path(r"^$", FoodApi.as_view(), name="food-list"),
]
