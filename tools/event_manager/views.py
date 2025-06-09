# coding: utf-8

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .models import HolidayCalendar
from .forms import HolidayCalendarForm,HolidayCalendarDeleteForm,HolidayCalendarUpdateForm
import datetime
import jpholiday
# from .serializer import CreditorSerializer,SupplierSerializer
# from .models import Creditor,Supplier
# from .forms import CreditorForm,CreditorUpdateForm,CreditorDeleteForm,SupplierForm,SupplierUpdateForm,SupplierDeleteForm



class CalendarView(LoginRequiredMixin,TemplateView):
    template_name = "event_manager/calendar.html"

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '公民館ツール：日程管理'
        return context


class HolidayCalendarListView(LoginRequiredMixin,ListView):
    template_name = "event_manager/HolidayCalendar.html"
    success_url = reverse_lazy('event_manager:holiday')
    model = HolidayCalendar

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        today = datetime.date.today()
        context['page_title'] = '休館日設定('+today.strftime('%Y')+'年)'
        context['form'] = HolidayCalendarForm()    # Create Modal画面
        context['form_update'] = HolidayCalendarUpdateForm()    # Update Modal画面
        context['form_delete'] = HolidayCalendarDeleteForm()    # Delete Modal画面
        return context

    def post(self, request):
        today = datetime.date.today()
        print(jpholiday.year_holidays(today.year))
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarCreateView(LoginRequiredMixin,CreateView):
    model = HolidayCalendar
    form_class = HolidayCalendarForm
    success_url = reverse_lazy('event_manager:HolidayCalendar')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarUpdateView(LoginRequiredMixin,UpdateView):
    model = HolidayCalendar
    form_class = HolidayCalendarUpdateForm
    success_url = reverse_lazy('event_manager:HolidayCalendar')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarDeleteView(LoginRequiredMixin,DeleteView):
    model = HolidayCalendar
    success_url = reverse_lazy('event_manager:HolidayCalendar')
