# coding: utf-8

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .models import RegularHoliday
from .serializer import RegularHolidaySerializer
from .forms import RegularHolidayForm,RegularHolidayDeleteForm,RegularHolidayUpdateForm

class SettingsView(LoginRequiredMixin,TemplateView):
    template_name = "common/settings.html"

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '各種設定'
        return context



class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "common/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '各種処理一覧'
        return context


# 会計年度情報
class RegularHolidayListView(LoginRequiredMixin,ListView):
    template_name = "common/regularholiday.html"
    model = RegularHoliday

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '定期休館日'
        context['form'] = RegularHolidayForm()    # Create Modal画面
        context['form_update'] = RegularHolidayUpdateForm()    # Update Modal画面
        context['form_delete'] = RegularHolidayDeleteForm()    # Delete Modal画面
        return context

class ModalRegularHolidayCreateView(LoginRequiredMixin,CreateView):
    model = RegularHoliday
    form_class = RegularHolidayForm
    success_url = reverse_lazy('common:regularholiday')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalRegularHolidayUpdateView(LoginRequiredMixin,UpdateView):
    model = RegularHoliday
    form_class = RegularHolidayUpdateForm
    success_url = reverse_lazy('common:regularholiday')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalRegularHolidayDeleteView(LoginRequiredMixin,DeleteView):
    model = RegularHoliday
    success_url = reverse_lazy('common:regularholiday')

class RegularHolidayApiView(viewsets.ModelViewSet):
    queryset = RegularHoliday.objects.all()
    serializer_class = RegularHolidaySerializer