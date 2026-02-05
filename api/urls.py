from django.urls import path

from .views import CategoriesView, CategoryDetailView


urlpatterns = [
    path('categories/', CategoriesView.as_view()),
    path('categories/<int:pk>', CategoryDetailView.as_view()),
]
