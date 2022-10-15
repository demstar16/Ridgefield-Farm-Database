from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.viewProfile, name="profile"),
    path('search/', views.search, name="search"),
    path('browse/', views.browse, name="browse"),
    path('paddock/<str:pk>/', views.byPaddock, name="paddock"),
    path('tag/<str:pk>/', views.byTag, name="tag"),
    path('year/<int:pk>/', views.byYear, name="year"),
    path('recently_deleted/', views.viewRecentlyDeleted, name="recently_deleted"),
    path('error/', views.errorPage, name="error"),
    path('profile/<int:pk>/edit', views.editProfile, name="edit_profile"),

]