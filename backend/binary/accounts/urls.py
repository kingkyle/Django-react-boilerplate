from django.urls import path, include

from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('', include('knox.urls')),
    path('login', LoginAPI.as_view()),
    path('register', RegisterAPI.as_view())
]
