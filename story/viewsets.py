from rest_framework.viewsets import ModelViewSet

from authx.permissions import IsBaristaUser

from .models import Ingredient
from .serializers import BaristaIngredientSerializer, ManagerIngredientSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = [IsBaristaUser]

    def get_serializer_class(self):
        if self.request.user.role > 2:
            return ManagerIngredientSerializer
        else:
            return BaristaIngredientSerializer
