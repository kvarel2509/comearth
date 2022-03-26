from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Pattern
from .serializers import PatternSerializer


class PatternViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Pattern.objects.all().order_by('-count_variable')
    serializer_class = PatternSerializer