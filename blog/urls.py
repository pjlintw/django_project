from django.urls import path
from . import views

urlpatterns = [
    # leave it as empty path
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]