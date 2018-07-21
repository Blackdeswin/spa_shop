from rest_framework import viewsets
from .serializers import *


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsPreviewSerializer
        return ProductsDetailSerializer
