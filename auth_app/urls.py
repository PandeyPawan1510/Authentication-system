from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name=""), 
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path("crud",views.crud),
    path('change_password', views.change_password, name='change_password'),
    path('password_reset',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

]

