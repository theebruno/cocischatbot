from os import path
import json

from django.http import JsonResponse
from .models import Course

data = ''


def json_courses(request):
    global data
    data = list(Course.objects.values())
    return JsonResponse(data, safe=False)


json_courses('request')

f = open("intents_courses.json", "w+")
f.write(f"""{data}""")
f.close()
