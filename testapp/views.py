from django.shortcuts import render
from .serializers import studentserializers
from .models import student
from rest_framework import viewsets

class stulist(viewsets.ModelViewSet):
    queryset =student.objects.all()
    serializer_class=studentserializers
