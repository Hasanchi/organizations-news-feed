from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path(
      'logout/',
      LogoutView.as_view(template_name='accounts/logout.html'),
      name='logout'
    ),
    path(
      'login/',
      LoginView.as_view(template_name='accounts/login.html'),
      name='login'
    ),
]
