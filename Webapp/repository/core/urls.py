from django.contrib import admin
from django.urls import path, include
from . import views
from .views import SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path("", include("django.contrib.auth.urls")),
    path('register/', SignUpView.as_view(), name="register"),
    path('profile/<str:pk>/', views.viewProfile, name="profile"),
    path('paddock/<str:pk>/', views.viewPaddock, name="paddock"),
    path('file/<str:pk>/', views.viewFile, name="file"),
    path('search/', views.search, name="search"),
    path('upload/', views.upload, name="upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)