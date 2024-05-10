from rest_framework import serializers
from music.models import Album, Artist, Song
from products.models import Product, Category, Bestsellers, FeaturedItems
from users.models import Comments, Problems, UserProfile
from django.contrib.auth.models import User


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'age', 'image']


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['name', 'artist', 'created', 'image']


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['title', 'artist', 'created', 'duration', 'music']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'count']


class BestsellersSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Bestsellers
        fields = ['name', 'product']


class FeaturedItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FeaturedItems
        fields = ['name', 'product', 'chegirma']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['user', 'comment_title', 'comment']


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ['firstname', 'email', 'problem_name', 'problem_description']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'age', 'image']



