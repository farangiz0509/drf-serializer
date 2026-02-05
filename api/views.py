from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Category
from .serializers import CategorySerializer


class CategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
