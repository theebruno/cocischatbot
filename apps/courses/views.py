from braces import views as bracesviews

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from .forms import CourseForm, CourseEditForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Course


# @method_decorator(login_required, name='dispatch')
# class CourseCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
class CourseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'courses/courses.html'
    model = Course
    form_class = CourseForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        all_courses = Course.objects.all()
        courses = all_courses.order_by('-updated')[:25]

        context = {'courses': courses, 'form': form}
        return render(request, self.template_name, context)

    def course(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            return redirect(reverse('courses:courses'))

        return redirect(reverse('courses:courses'))


class CourseListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Course.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CourseListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = CourseForm()
        context['create_url'] = reverse_lazy("courses:courses")
        return context


# # @method_decorator(login_required, name='dispatch')
# class CourseDetailView(LoginRequiredMixin, DetailView):
#     model = Course
#     template_name = 'courses/course_detail.html'


# @method_decorator(login_required, name='dispatch')
class CourseUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    template_name = 'courses/course_update.html'
    model = Course
    form_class = CourseEditForm


# @method_decorator(login_required, name='dispatch')
class CourseDelete(LoginRequiredMixin, DeleteView):
    template_name = 'courses/course_delete.html'
    model = Course
    # messages.success('Successfully deleted course')    research on this one...
    success_url = reverse_lazy('courses:courses')
