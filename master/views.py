import re

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .models import Pattern
from .serializers import PATTERN2
from .serializers import PatternSerializer, GenerateSerializer


class PatternViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Pattern.objects.all().order_by('-count_variable')
    serializer_class = PatternSerializer

    @staticmethod
    def change(string, data):
        return data.get(string[2:-1], '<no data>')

    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def generation(self, request, pk):
        pattern = self.get_object()

        serializer = GenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = [self.change(i, serializer.validated_data['data']) if re.fullmatch(PATTERN2, i)
                  else i for i in pattern.prepared]
        return Response({'result': ''.join(result)})
