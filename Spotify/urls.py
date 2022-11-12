
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from music.views import *

router = DefaultRouter()
router.register("albomlar",AlbomViewSet)
router.register("qoshiqlar",SongViewSet)
router.register("qoshiqchi",SingerViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('token/', obtain_auth_token, name='token'),
    # path('hello/',HelloAPI.as_view()),
    # path('singers/',SingerAPIView.as_view()),
    # path('songs/',SongsAPIView.as_view()),
    # path('song/<int:pk>/',SongAPIView.as_view()),
    # path('alboms/',AlbomsAPIView.as_view()),
    # path('singer/<int:pk>/',SongerAPIView.as_view()),
    # path('albom/<int:pk>/',OnealbomAPIView.as_view()),
]
