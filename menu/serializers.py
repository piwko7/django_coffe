from rest_framework.serializers import ModelSerializer

from story.serializers import BaristaIngredientSerializer, ManagerIngredientSerializer

from .models import Component, Menu, MenuItem


class BaseComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = "__all__"


class BaseItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class BaseMenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class ManagerComponentSerializer(BaseComponentSerializer):
    ingredient = ManagerIngredientSerializer(read_only=True)


class ComponentSerializer(BaseComponentSerializer):
    ingredient = BaristaIngredientSerializer(read_only=True)
