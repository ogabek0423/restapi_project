from django.shortcuts import render, redirect
from .models import Album, Artist, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class TestApiView(APIView):

    def get(self, request):
        return Response({'message': 'test api xabari'})

#
# class AlbumViewSet(ModelViewSet):
#
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#     # permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     filter_backends = [filters.SearchFilter,]
#     search_fields = ['=name', '^name', '$name', '#name', '@name',  'artist__first_name', '$artist__first_name',
#                      '^artist__first_name', '#artist__first_name', '@artist__first_name', 'artist__last_name',
#                      '^artist__last_name', '=artist__last_name', '$artist__last_name',]
#     pagination_class = LimitOffsetPagination
#
#
# class ArtistViewSet(ModelViewSet):
#
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     # permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     filter_backends = [filters.SearchFilter,]
#     search_fields = ['first_name', 'last_name', '^first_name', '^last_name', '$first_name', '$last_name',
#                      '@first_name', '@last_name', '=first_name', '=last_name',]
#     pagination_class = LimitOffsetPagination
#
#
# class SongViewSet(ModelViewSet):
#
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
#     # permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     filter_backends = [filters.SearchFilter, ]
#     search_fields = ['title', '^title', '$title', '#title', '^artist__first_name', '^artist__last_name',
#                      '$artist__first_name', '$artist__last_name', '@artist__first_name', '@artist__last_name',]
#     pagination_class = LimitOffsetPagination
