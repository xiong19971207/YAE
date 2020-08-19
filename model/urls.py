from django.urls import path

from model import views

urlpatterns = [
    path('showall/',views.showall)
]