from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from users.views import (LoginAPI, get_current_user, users_api ,user_detail)

urlpatterns = [
    path('', users_api),
    path('<int:pk>/', user_detail),
    path('login/', LoginAPI.as_view(), name= 'login'),
    path('currentuser/', get_current_user, name= 'current user'),
]