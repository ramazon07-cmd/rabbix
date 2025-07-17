from celery import shared_task
from .models import Video
import time
from django.core.mail import send_mail

@shared_task(bind=True)
def process_video(self, video_id):
    video = Video.objects.get(id=video_id)
    video.status = 'processing'
    video.save()

    # ⏳ Simulyatsiya: AI video processing
    time.sleep(15)

    video.status = 'done'
    video.save()

    # ✅ Email yuborish
    send_done_email(video.user.email)  # Foydalanuvchi emailini olamiz

    return f"Video {video_id} processed and email sent!"  # ⚡️ Task natijasi

def send_done_email(email):
    send_mail(
        'Your video is ready!',
        'Thank you for using Rabbix. Your video processing is complete.',
        'noreply@rabbix.com',
        [email],
        fail_silently=False,
    )
