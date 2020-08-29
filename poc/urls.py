from django.urls import path
from . import views

urlpatterns = [
    path('rest', views.ProductList.as_view(), name='ProductList') #filtering using rest_framework
]