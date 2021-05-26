from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from . models import mutual
from .serializers import employeeSerializers
# Create your views here.

class Mutual_Fund_List(ListAPIView):

    queryset = mutual.objects.all()
    serializer_class = employeeSerializers

