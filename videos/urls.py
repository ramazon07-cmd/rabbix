from django.urls import path, include
from rest_framework.routers import DefaultRouter
from videos.views import VideoViewSet

router = DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
