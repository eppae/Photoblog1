from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.sign_in,name='login'),
    path('logout/',views.sign_out,name='logout'),
    path('register/',views.sign_up,name='register'),
    path('forgot/',views.forgot,name='forgot'),
    path('user/editprofile/',views.edit_profile,name='edit-profile'),
    path('user/notifications/',views.edit_notifications,name='notifications'),
    path('user/connections/',views.edit_connections,name='connections'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]