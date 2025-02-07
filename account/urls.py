from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    # main page after login
    path('profile/', views.profile, name='profile'),

    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    url(r'login_success/$', views.login_success, name='login_success')
]

# these are the URLs that come packaged with include('django.contrib.auth.urls'):
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
