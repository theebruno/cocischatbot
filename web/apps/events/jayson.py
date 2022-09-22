from os import path
import json

from django.http import JsonResponse

from .models import Event

data = ''


def json_events(request):
    global data
    data = list(Event.objects.values())
    return JsonResponse(data, safe=False)


json_events('request')

f = open("intents_events.json", "w+")
f.write(f"""{data}""")
f.close()
