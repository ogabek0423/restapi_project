from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, AlbumViewSet
from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(prefix='songs', viewset=SongViewSet)
# router.register(prefix='artists', viewset=ArtistViewSet)
# router.register(prefix='albums', viewset=AlbumViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]