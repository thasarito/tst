from django.shortcuts import render
from rest_framework import viewsets, pagination, generics, filters
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .models import Dictionary
from .serializers import DictionarySerializer
from django.http import request

class DictionaryPagination(pagination.PageNumberPagination):
    page_size = 10
    
class DictionaryView(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all().order_by('-up')
    serializer_class = DictionarySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'meaning',)
    pagination_class = DictionaryPagination


    @list_route()
    def percUp_list(self, request):
        q = sorted(list(self.get_queryset()), key= lambda obj: -obj.percentUp())
        page = self.paginate_queryset(q)
        if page is not None:
        	serializer=self.get_serializer(page, many=True)
        	return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(q, many=True)
        return Response(serializer.data)
