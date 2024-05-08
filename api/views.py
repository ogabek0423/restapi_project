from django.shortcuts import render, redirect
from products.models import Category, Product, Bestsellers, FeaturedItems
from music.models import Album, Artist, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Problems, Comments
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer, CategorySerializer, ProductSerializer
from .serializers import BestsellersSerializer, FeaturedItemsSerializer, CommentsSerializer
from .serializers import ProblemsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', '^name', 'artist__first_name',
                     '^artist__first_name', 'artist__last_name',
                     '^artist__last_name', '=artist__last_name', ]
    pagination_class = LimitOffsetPagination


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', '^first_name', '^last_name', '=first_name', '=last_name',]
    pagination_class = LimitOffsetPagination


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', '^title', '^artist__first_name', '^artist__last_name',]
    pagination_class = LimitOffsetPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = LimitOffsetPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'price',]
    pagination_class = LimitOffsetPagination


class BestsellerViewSet(ModelViewSet):
    queryset = Bestsellers.objects.all()
    serializer_class = BestsellersSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'product__name', 'product__description']
    pagination_class = LimitOffsetPagination


class FavoriteViewSet(ModelViewSet):
    queryset = FeaturedItems.objects.all()
    serializer_class = FeaturedItemsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'product__name', 'product__description', 'chegirma']
    pagination_class = LimitOffsetPagination


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['comment', 'comment_title']
    pagination_class = LimitOffsetPagination


class ProblemViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['problem_name', 'problem_description', ]
    pagination_class = LimitOffsetPagination



