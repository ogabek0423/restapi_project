from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, AlbumViewSet, CategoryViewSet, ProductViewSet, BestsellerViewSet
from .views import FavoriteViewSet, CommentViewSet, ProblemViewSet, UserProfileViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        description="Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

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
router.register(prefix='userprofile', viewset=UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),

]


