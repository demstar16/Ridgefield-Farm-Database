from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.viewProfile, name="profile"),
    path('paddock/<str:pk>/', views.viewPaddock, name="paddock"),
    path('search/', views.search, name="search"),
]