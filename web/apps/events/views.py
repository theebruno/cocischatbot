from braces import views as bracesviews

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.contrib.auth import get_user_model

from .forms import EventForm, EventEditForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Event
from apps.course_units.models import CourseUnit
from apps.event_organisers.models import EventOrganiser


User = get_user_model()


# @method_decorator(login_required, name='dispatch')
# class EventCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'events/events.html'
    model = Event
    form_class = EventForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        all_events = Event.objects.all()
        events = all_events.order_by('-updated')[:25]

        context = {'events': events, 'form': form}
        return render(request, self.template_name, context)

    def event(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            return redirect(reverse('events:events'))

        return redirect(reverse('events:events'))


class EventListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Event.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = EventForm()
        context['create_url'] = reverse_lazy("events:events")
        return context


# # @method_decorator(login_required, name='dispatch')
# class EventDetailView(LoginRequiredMixin, DetailView):
#     model = Event
#     template_name = 'events/event_detail.html'


# @method_decorator(login_required, name='dispatch')
class EventUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    template_name = 'events/event_update.html'
    model = Event
    form_class = EventEditForm


# @method_decorator(login_required, name='dispatch')
class EventDelete(LoginRequiredMixin, DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    # messages.success('Successfully deleted event')    research on this one...
    success_url = reverse_lazy('events:events')
