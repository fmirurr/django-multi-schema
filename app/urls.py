from django.urls import include, path
from django.contrib import admin

from .views import App_ApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", App_ApiView.as_view()),
]
