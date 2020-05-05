from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, LogoutView
from .views import ProfileDetailView

urlpatterns = [
    path('', ProfileDetailView.as_view(), name="detail"),

    path('login/', LoginView.as_view(template_name='user/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    
    path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset.html', email_template_name='user/password_reset_email.html', success_url=reverse_lazy('user:password_reset_done')), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html', success_url=reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

]
