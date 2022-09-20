from django.urls import path, re_path
from apps.profiles import views

urlpatterns = [
    # profile/..
    path('me/', views.ProfileDetailView.as_view(), name='show_self'),

    path('me/', views.EditProfile.as_view(), name='show_self'),

    path('(<username>', views.ProfileDetailView.as_view(), name='show'),
]
