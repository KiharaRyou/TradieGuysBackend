from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from users.views import (LoginAPI, get_current_user, registration_api)

urlpatterns = [
    # path('login/', obtain_auth_token, name= 'login'),
    path('login/', LoginAPI.as_view(), name= 'login'),
    path('currentuser/', get_current_user, name= 'current user'),
    path('register/', registration_api, name= 'register'),
]