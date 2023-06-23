from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.dish_search, name='search'),
]
