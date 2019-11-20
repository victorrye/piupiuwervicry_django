from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('profile/', views.profile, name='blog-profile'),
]

