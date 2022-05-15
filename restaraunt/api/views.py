from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="internal_code"
    )

    class Meta:
        model = Food
        fields = (
            "is_publish",
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional",
        )


class FoodListSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField("get_foods")

    def get_foods(self, category):
        """
        Get only published foods.
        """
        qs = Food.objects.filter(is_publish=True, category=category)
        serializer = FoodSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = FoodCategory
        fields = ("id", "name_ru", "name_en", "name_ch", "order_id", "foods")


class FoodApi(APIView):
    """
    Retrieve food categories and food inside that categories.
    """

    def get(self, request):
        foodcategorшes = FoodCategory.objects.filter(food__is_publish=True)
        serializer = FoodListSerializer(foodcategorшes, many=True)
        return Response(serializer.data)
