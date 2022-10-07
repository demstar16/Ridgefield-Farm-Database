from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('request_submitted/', views.submitted, name='submitted'),

    path('audit_list/', views.audit_list, name='audit_list'),
    path('audit_activate/<str:pk>/', views.audit_activate, name='audit_activate'),
    path('audit_freeze/<str:pk>/', views.audit_freeze, name='audit_freeze'),
    path('confirm_deletion/<str:pk>/', views.confirm_deletion, name='confirm_deletion'),
    path('delete/<str:pk>/', views.delete_account, name='delete_account'),

    
    #To enable to send a email from host email, you need to go to 
    #bottom of setting.py to change SMTP config 
    #EMAIL_HOST_USER is the host email(need to be gmail for current config)
    #EMAIL_HOST_PASSWORD due to sercurity update of the gmail, some work around is needed
    #1. go to gmail click google account logo and go to Manage your google account
    #2. go to sercurity, to be noted is that 2-set verification need to be enable 
    #3. Click app password, copy app pasword from the webpage to EMAIL_HOST_PASSWORD
    
    
    #Submit email form
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"), name = "reset_password"),
    
    #Email sent success message
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name = "password_reset_done"),
    
    #Link to password to email
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    
    #Password successfully changed meassge
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name = "password_reset_complete"),
    
    
]
