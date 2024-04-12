from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.blog, name='posts')
]
