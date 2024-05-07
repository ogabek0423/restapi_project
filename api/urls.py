from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, AlbumViewSet, CategoryViewSet, ProductViewSet, BestsellerViewSet
from .views import FavoriteViewSet, CommentViewSet, ProblemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='songs', viewset=SongViewSet)
router.register(prefix='artists', viewset=ArtistViewSet)
router.register(prefix='albums', viewset=AlbumViewSet)
router.register(prefix='category', viewset=CategoryViewSet)
router.register(prefix='products', viewset=ProductViewSet)
router.register(prefix='bestseller', viewset=BestsellerViewSet)
router.register(prefix='favorite', viewset=FavoriteViewSet)
router.register(prefix='comment', viewset=CommentViewSet)
router.register(prefix='problem', viewset=ProblemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]