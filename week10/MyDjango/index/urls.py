from django.urls import path, re_path, register_converter
from . import views, converters

urlpatterns = [
    path('index', views.index),
    # path('login', views.login),
    path('login', views.login2)
]
