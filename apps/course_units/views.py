from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView

from .forms import CourseUnitForm, CourseUnitEditForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import CourseUnit


# @method_decorator(login_required, name='dispatch')
class CourseUnitCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    template_name = 'course_units/course_units.html'
    model = CourseUnit
    form_class = CourseUnitForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        all_course_units = CourseUnit.objects.all()
        course_units = all_course_units.order_by('-edited_date')[:25]

        context = {'course_units': course_units, 'form': form}
        return render(request, self.template_name, context)

    def course_unit(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            return redirect(reverse('course_units:course_units'))

        return redirect(reverse('course_units:course_units'))


class CourseUnitListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = CourseUnit.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CourseUnitListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = CourseUnitForm()
        context['create_url'] = reverse_lazy("course_units:course_units")
        return context


# # @method_decorator(login_required, name='dispatch')
# class CourseUnitDetailView(LoginRequiredMixin, DetailView):
#     model = CourseUnit
#     template_name = 'course_units/course_detail.html'


# @method_decorator(login_required, name='dispatch')
class CourseUnitUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    template_name = 'course_units/course_update.html'
    model = CourseUnit
    form_class = CourseUnitEditForm


# @method_decorator(login_required, name='dispatch')
class CourseUnitDelete(LoginRequiredMixin, DeleteView):
    template_name = 'course_units/course_delete.html'
    model = CourseUnit
    # messages.success('Successfully deleted course_unit')    research on this one...
    success_url = reverse_lazy('course_units:course_units')
