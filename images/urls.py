from django.urls import path
from images.views import (image_upload)

urlpatterns = [
    path('uploadimage/', image_upload, name='upload_image'),
]