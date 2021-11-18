from django.shortcuts import render
from rest_framework import generics, viewsets, status, exceptions, filters
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms import models 
from . import permissions
from . import serializers


class DetailRoomView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly,]

    def perform_update(self, serializer):
        old_progress = serializer.instance.creation_progress
        instance = serializer.save()
        new_progress = instance.creation_progress
        if old_progress >= new_progress:
            serializer.save(creation_progress=old_progress)

class ListRoomView(generics.ListCreateAPIView):
    queryset = models.Room.objects.all().order_by('price')[0:8]
    serializer_class = serializers.RoomSerializer
    def get_queryset(self):
        return models.Room.objects.filter(published=True).order_by('price')[0:8]
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserListRoomView(generics.ListCreateAPIView):
    queryset = models.Room.objects.all().order_by('-id')
    serializer_class = serializers.RoomSerializer
    def get_queryset(self):
        return models.Room.objects.filter(owner=self.request.user,published=True).order_by('-id')
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SearchListRoomView(generics.ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','position_full_address','position_locality_regione']
    def get_queryset(self):
        return models.Room.objects.filter(published=True).order_by('-id')
    parser_classes = (MultiPartParser,)

class RoomImageView(generics.CreateAPIView):
    
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.RoomImageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    
    def perform_create(self, serializer):
        if serializer.validated_data['room'].owner != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa inserzione')
        if serializer.is_valid():
            serializer.save()


class DetailRoomImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RoomImage.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.RoomImageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    def perform_delete(self, serializer):
        if serializer.validated_data['room'].owner != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa inserzione')
        serializer.save()