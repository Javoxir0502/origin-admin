from django.urls import path
from .views import MahsulotAPI

urlpatterns = [
    path('', MahsulotAPI.as_view()),
]