from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.viewProfile, name="profile"),
    path('search/', views.search, name="search"),
    path('browse/', views.browse, name="browse"),
    path('browse/<str:pk>/', views.byPaddock, name="browse"),
    path('recently_deleted/', views.viewRecentlyDeleted, name="recently_deleted"),
]