from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import RegisterSerializer

@api_view(['POST'],)
def registration_api(request):
    serializers = RegisterSerializer(data=request.data)
    data = {}

    if serializers.is_valid():
        user =serializers.save()
        data['status'] = 'OK'
        data['email'] = user.email
        data['username'] = user.username
    else:
        data['status'] = 'Error'
        data['reasons'] = serializers.errors

    return Response(data)

class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'OK',
                'token': token.key,
                'email': user.email,
                'username': user.username,
                'is_admin': user.is_admin
            })
        else:
            return Response({
                'status': 'Error',
                'reason': 'Account does not exist or password is not correct'
            })

@api_view(['GET'])
def get_current_user(request):
    return Response({
        'username': request.user.username,
        'email': request.user.email,
        'is_admin': request.user.is_admin,
    })
