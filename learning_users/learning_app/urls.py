from django.contrib import admin
from django.urls import path
from django.urls import include, path
from learning_app import views

app_name = 'learning_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]