from rest_framework.decorators import api_view
from rest_framework.response import Response
from images.models import Image

@api_view(['POST'])
def image_upload(request):
    file = request.data['file']
    image = Image.objects.create(image=file)
    url = request.get_full_path()
    return Response({
        'status': 'OK',
        'url': image.image.url
    })
