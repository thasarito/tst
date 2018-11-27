from django.shortcuts import render
from rest_framework import viewsets, pagination, generics, filters
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import request
from django.contrib.auth.models import User

class DescriptionPagination(pagination.PageNumberPagination):
    page_size = 10
    
class DescriptionView(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('word', 'meaning',)
    pagination_class = DescriptionPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
    	return self.request.user