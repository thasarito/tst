from django.shortcuts import render
from rest_framework import viewsets, pagination, generics
from .models import Dictionary
from .serializers import DictionarySerializer

class DictionaryPagination(pagination.PageNumberPagination):
    page_size = 10
    
class DictionaryView(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    pagination_class = DictionaryPagination




# class DictionaryListView(generics.ListAPIView):
#     queryset = Dictionary.objects.all()
#     serializer_class = DictionarySerializer
#     pagination_class = DictionaryPagination
