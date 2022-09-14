"""
"""
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route

    # demo
    path("", include("apps.accounts.urls")),  # Auth routes - login / register
    path("", include("apps.home.urls")),

    # custom
    path("", include("apps.accounts.urls")),
    path("courses/", include("apps.courses.urls")),
    path("course_units/", include("apps.course_units.urls")),
    path("class_timetables/", include("apps.class_timetables.urls")),
    path("exam_timetables/", include("apps.exam_timetables.urls")),
    path("departments/", include("apps.departments.urls")),
    path("lecturer_offices/", include("apps.lecturer_offices.urls")),
    path("profile/", include("apps.profiles.urls")),
]
