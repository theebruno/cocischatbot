from django.http import JsonResponse
from .models import CourseUnit


def json_course_units(request):
    data = list(CourseUnit.objects.values())
    return JsonResponse(data.append('intents2.json'), safe=False)
