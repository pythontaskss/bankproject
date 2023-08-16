from .import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('detail/',views.detail,name='detail'),
    path('new/',views.new,name='new'),
    path('form/',views.form,name='form'),

]