"""
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth import get_user_model

from apps.course_units.models import CourseUnit
from apps.event_organisers.models import EventOrganiser
from apps.events.models import Event

User = get_user_model()


@login_required(login_url="/login/")
def index(request):
    total_users_registered = User.objects.count()
    total_events = Event.objects.count()
    total_event_organisers = EventOrganiser.objects.count()
    # print("--------------------------------")
    # print(total_event_organisers)
    # print("--------------------------------")
    context = {
        'segment': 'index',
        'total_users_registered': total_users_registered,
        'total_events': total_events,
        'total_event_organisers': total_event_organisers,
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
