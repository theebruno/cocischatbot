from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView, TemplateView

from .forms import ClassTimetableForm, ClassTimetableEditForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import ClassTimetable


class ClassTimetableListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = ClassTimetable.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ClassTimetableListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = ClassTimetableForm()
        context['create_url'] = reverse_lazy("class_timetables:class_timetables")
        return context


# # @method_decorator(login_required, name='dispatch')
# class ClassTimetableDetailView(LoginRequiredMixin, DetailView):
#     model = ClassTimetable
#     template_name = 'class_timetables/course_detail.html'


# @method_decorator(login_required, name='dispatch')
class ClassTimetableUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    template_name = 'class_timetables/class_timetables_update.html'
    model = ClassTimetable
    form_class = ClassTimetableEditForm


# @method_decorator(login_required, name='dispatch')
class ClassTimetableDelete(LoginRequiredMixin, DeleteView):
    template_name = 'class_timetables/course_delete.html'
    model = ClassTimetable
    # messages.success('Successfully deleted class_timetable')    research on this one...
    success_url = reverse_lazy('class_timetables:class_timetables')
