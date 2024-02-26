from django.urls import path
from .views import User_ViewSet, UserLogin_ViewSet

app_name = 'users'

urlpatterns = [
    path('user/login', UserLogin_ViewSet.as_view()),
    path('user', User_ViewSet.as_view()),
]
