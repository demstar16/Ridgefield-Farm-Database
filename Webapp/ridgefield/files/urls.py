from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path('id/<str:pk>/', views.viewFile, name="file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)