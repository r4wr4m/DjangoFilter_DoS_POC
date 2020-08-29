from django.shortcuts import render
from django.http import HttpResponse
#added: 
#from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from poc.models import Product



#Filtering using rest_framework
#https://www.django-rest-framework.org/api-guide/filtering/
#it's using django_filters library
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'price']