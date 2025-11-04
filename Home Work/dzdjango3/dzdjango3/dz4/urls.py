from django.urls import path
from . import views

urlpatterns = [
    path('', views.dz4, name='dz4'),
    path('<int:dz_id>', views.detail, name='detail'),
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),
    path('current/', views.current, name='current'),

]
