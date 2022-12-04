from rest_framework.serializers import ModelSerializer, SlugRelatedField

from supplier.serializers import AdminSupplierSerializer

from .models import Ingredient


class BaseIngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class BaristaIngredientSerializer(BaseIngredientSerializer):
    supplier = SlugRelatedField(read_only=True, slug_field="custom_id")


class ManagerIngredientSerializer(BaseIngredientSerializer):
    supplier = AdminSupplierSerializer()
