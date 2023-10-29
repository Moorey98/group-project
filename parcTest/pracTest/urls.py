from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'parcTest'  

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('listings/', views.listingspage, name='listingspage'),
    path('login/', views.loginpage, name='loginpage'),
    path('signup/', views.signuppage, name='signuppage'),
    path("admin/", admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('userpage/', views.userpage, name='userpage')

]
