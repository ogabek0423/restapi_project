from rest_framework import serializers
from music.models import Album, Artist, Song
from products.models import Product, Category, Bestsellers, FeaturedItems
from users.models import Comments, Problems, UserProfile
from django.contrib.auth.models import User


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'age', 'image', 'page_views', 'created']


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'created', 'image', 'views']


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'created', 'duration', 'music', 'listens']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'count']


class BestsellersSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Bestsellers
        fields = ['id', 'name', 'product', 'views']


class FeaturedItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FeaturedItems
        fields = ['id', 'name', 'product', 'chegirma']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment_title', 'comment', 'created']


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description', 'created_at',]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'age', 'image', 'creation_date']



