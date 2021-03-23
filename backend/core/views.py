from rest_framework import viewsets
from backend.core.models import Category
from backend.core.serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
