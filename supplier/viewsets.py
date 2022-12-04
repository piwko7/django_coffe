from rest_framework.viewsets import ModelViewSet

from authx.permissions import IsManagerUser

from .models import Supplier
from .serializers import AdminSupplierSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    permission_classes = [IsManagerUser]
    serializer_class = AdminSupplierSerializer
