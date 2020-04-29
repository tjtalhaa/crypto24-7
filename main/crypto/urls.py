from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
]
