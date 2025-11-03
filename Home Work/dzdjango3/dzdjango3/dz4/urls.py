from django.urls import path
from . import views

urlpatterns = [
    path('', views.dz4, name='dz4')
]
