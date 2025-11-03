from django.urls import path
from . import views

urlpatterns = [
    path('', views.dz4, name='dz4'),
    path('<int:dz_id>', views.detail, name='detail'),

]
