from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', views.registration, name="registration"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # TODO: разобраться, почему не работает код с 'logout/'
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
