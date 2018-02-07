# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import WaterRecord
from .serializers import WaterRecordSerializer

# APIView
class WaterRecordList(APIView):
    def get(self, request, format=None):
        items = WaterRecord.objects.all()
        serializer = WaterRecordSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = WaterRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ListCreateAPIView
class WaterRecordListCreate(generics.ListCreateAPIView):
    queryset = WaterRecord.objects.all()
    serializer_class = WaterRecordSerializer

# api_view
@api_view(['GET', 'POST'])
def water_record_list(request):
    '''
    List all items or create a new item
    '''
    if request.method == 'GET':
        items = WaterRecord.objects.all()
        serializer = WaterRecordSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WaterRecordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def water_record_detail(request, pk):
    try:
        item = WaterRecord.objects.get(pk=pk)
    except WaterRecord.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WaterRecordSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WaterRecordSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)