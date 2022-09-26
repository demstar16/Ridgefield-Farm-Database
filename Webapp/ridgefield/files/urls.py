from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path('id/<str:pk>/', views.viewFile, name="file"),
    path('delete_confirm/<str:pk>/', views.delete_confirm, name="delete_confirm"),
    path('file_delete/<str:pk>/', views.file_delete, name='file_delete'),
    path('fileRestore/<str:pk>/', views.fileRestore, name='fileRestore'),
    path('permenantDelete/<str:pk>/', views.permanentDelete, name='permanentDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)