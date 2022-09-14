"""
"""
from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # /
    path('', views.index, name='home'),
]
