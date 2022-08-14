from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Entity
from .serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        data = dict(request.data)
        data['created_by'] = request.user.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)