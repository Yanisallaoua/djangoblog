from django.urls import path
from . import views
from .views import NewPost

urlpatterns = [
    
    path('', views.home, name= 'blog-home' ),
    path('npost/', NewPost.as_view(), name= 'blog-post' ),



]