
from django.contrib import admin
from django.urls import path, include, re_path
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index/', views.index, name= 'index'),
    path('help/', views.help, name='help'),
    path('', views.index, name= 'index'),
]