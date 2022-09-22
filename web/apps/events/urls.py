"""
"""
from django.urls import path, re_path

from apps.events import views
from .jayson import json_events

urlpatterns = [
    # events/
    path('create/', views.EventCreateView.as_view(), name='events_create'),
    path('list/', views.EventListView.as_view(), name='events'),

    path('list/json/', json_events, name='json_events'),
]
