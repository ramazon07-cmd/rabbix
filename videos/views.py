from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_video

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        video_id = response.data['id']
        process_video.delay(video_id)
        return response
