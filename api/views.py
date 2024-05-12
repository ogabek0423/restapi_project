from django.shortcuts import render, redirect
from products.models import Category, Product, Bestsellers, FeaturedItems
from music.models import Album, Artist, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Problems, Comments, UserProfile
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer, CategorySerializer, ProductSerializer
from .serializers import BestsellersSerializer, FeaturedItemsSerializer, CommentsSerializer
from .serializers import ProblemsSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.db.transaction import atomic



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

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        album = self.get_object()
        serializer = AlbumSerializer(album, many=False)
        created = album.created
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        album = self.get_object()
        serializer = AlbumSerializer(album, many=False)
        updated = album.updated
        return Response(data={'updated': updated}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        album = self.get_object()
        with atomic():
            album.views = album.views + 1
            album.save()
            return Response(status.HTTP_204_NO_CONTENT)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', '^first_name', '^last_name', '=first_name', '=last_name',]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = ArtistSerializer(artist, many=False)
        created = artist.created
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def listens(self, request, *args, **kwargs):
        artist = self.get_object()
        with atomic():
            artist.page_views = artist.page_views + 1
            artist.save()
            return Response(status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def ages(self, request, *args, **kwargs):
        artist = self.get_queryset()
        artist = artist.order_by('age')
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', '^title', '^artist__first_name', '^artist__last_name',]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def listens(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listens = song.listens + 1
            song.save()
            return Response(status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listens')
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def maxlength(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-duration')
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def categories(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        count = queryset.count()
        return Response(data={'count': count}, status=status.HTTP_200_OK)

    # category modelda fieldlar kamligi uchun actionlar kam

    @action(detail=False, methods=['GET'])
    def lists(self, request, *args, **kwargs):
        category = self.get_queryset()
        serializer = CategorySerializer(category, many=True)
        queryset = category.order_by('name')
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'price',]
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def most_exp(self, request, *args, **kwargs):
        product = self.get_queryset()
        product = product.order_by('-price')
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def most_products(self, request, *args, **kwargs):
        product = self.get_queryset()
        product = product.order_by('-count')
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abc_list(self, request, *args, **kwargs):
        product = self.get_queryset()
        product = product.order_by('name')
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class BestsellerViewSet(ModelViewSet):
    queryset = Bestsellers.objects.all()
    serializer_class = BestsellersSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'product__name', 'product__description']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def bests(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.order_by('-product__count')
        serializer = BestsellersSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        bestp = self.get_object()
        with atomic():
            bestp.views = bestp.views + 1
            bestp.save()
            return Response(status.HTTP_204_NO_CONTENT)



class FavoriteViewSet(ModelViewSet):
    queryset = FeaturedItems.objects.all()
    serializer_class = FeaturedItemsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'product__name', 'product__description', 'chegirma']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def cheaps(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.order_by('-chegirma')
        serializer = FeaturedItemsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abc_list(self, request, *args, **kwargs):
        favo = self.get_queryset()
        favo = favo.order_by('name')
        serializer = FeaturedItemsSerializer(favo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['comment', 'comment_title']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def user_ages(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.order_by('-user_id')
        serializer = CommentsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abc_list(self, request, *args, **kwargs):
        com = self.get_queryset()
        com = com.order_by('comment_title')
        serializer = CommentsSerializer(com, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def createdtime(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentsSerializer(comment, many=False)
        created = comment.created
        return Response(data={'created': created}, status=status.HTTP_200_OK)


class ProblemViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['problem_name', 'problem_description', ]
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def abc_list(self, request, *args, **kwargs):
        pro = self.get_queryset()
        pro = pro.order_by('problem_name')
        serializer = ProblemsSerializer(pro, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def older_problems(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProblemsSerializer(queryset, many=True)
        queryset = queryset.order_by('-created_at')
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAdminUser,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'age']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def opened(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = UserProfileSerializer(queryset, many=False)
        data = queryset.creation_date
        return Response(data={'created profile': data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def olders(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserProfileSerializer(queryset, many=True)
        queryset = queryset.order_by('-creation_date')
        return Response(data=serializer.data, status=status.HTTP_200_OK)





