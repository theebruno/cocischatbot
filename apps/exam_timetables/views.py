from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView

from .forms import ExamTimetableForm, ExamTimetableEditForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import ExamTimetable


# @method_decorator(login_required, name='dispatch')
class ExamTimetableCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    template_name = 'exam_timetables/exam_timetables.html'
    model = ExamTimetable
    form_class = ExamTimetableForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        all_exam_timetables = ExamTimetable.objects.all()
        exam_timetables = all_exam_timetables.order_by('-edited_date')[:25]

        context = {'exam_timetables': exam_timetables, 'form': form}
        return render(request, self.template_name, context)

    def exam_timetable(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            return redirect(reverse('exam_timetables:exam_timetables'))

        return redirect(reverse('exam_timetables:exam_timetables'))


class ExamTimetableListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = ExamTimetable.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ExamTimetableListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = ExamTimetableForm()
        context['create_url'] = reverse_lazy("exam_timetables:exam_timetables")
        return context


# # @method_decorator(login_required, name='dispatch')
# class ExamTimetableDetailView(LoginRequiredMixin, DetailView):
#     model = ExamTimetable
#     template_name = 'exam_timetables/course_detail.html'


# @method_decorator(login_required, name='dispatch')
class ExamTimetableUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    template_name = 'exam_timetables/course_update.html'
    model = ExamTimetable
    form_class = ExamTimetableEditForm


# @method_decorator(login_required, name='dispatch')
class ExamTimetableDelete(LoginRequiredMixin, DeleteView):
    template_name = 'exam_timetables/course_delete.html'
    model = ExamTimetable
    # messages.success('Successfully deleted exam_timetable')    research on this one...
    success_url = reverse_lazy('exam_timetables:exam_timetables')
