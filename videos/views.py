from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from .tasks import process_video
from drf_spectacular.utils import extend_schema

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @extend_schema(
        summary="🎥 Upload a video and trigger async processing",
        description="""
This endpoint accepts a video upload, saves it to the database,
and triggers an asynchronous task via RabbitMQ & Celery.

**Task logic:**
- Sets video status to `processing`
- Simulates 15s processing delay
- Sets status to `done`
- Sends email notification to the user

Broker: RabbitMQ 🐇
Backend: Redis 📦
Task: `process_video(video_id)` via Celery
        """,
        request=VideoSerializer,
        responses={201: VideoSerializer},
    )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        video_id = response.data['id']
        process_video.delay(video_id)
        return response
