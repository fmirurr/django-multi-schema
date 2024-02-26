from django.urls import path
from veterinary.view import Veterinary_ViewSet


app_name = 'veterinary'

urlpatterns = [
    path('veterinary/', Veterinary_ViewSet.as_view())
]
