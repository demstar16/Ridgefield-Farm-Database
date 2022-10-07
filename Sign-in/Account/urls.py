from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('request_submitted/', views.submitted, name='submitted'),

    path('audit_list/', views.audit_list, name='audit_list'),
    path('audit_activate/<str:pk>/', views.audit_activate, name='audit_activate'),
    path('audit_freeze/<str:pk>/', views.audit_freeze, name='audit_freeze')
]