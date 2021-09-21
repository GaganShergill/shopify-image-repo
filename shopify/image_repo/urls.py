from django.urls import path
from .views import *
from django.views import static
from django.conf import settings

app_name = 'image_repo'

urlpatterns = [
    path('', image_list_view, name='image_list'),
    path('upload/', image_upload_view, name='image_upload'),
    path('images/<path>', static.serve, {'document_root': settings.MEDIA_ROOT + '/images', }),
    path('register/', UserCreateView.as_view(), name='register'),
    path('about/', about_view, name='about'),
]
