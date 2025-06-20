# coding: utf-8

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .models import HolidayCalendar
from common.models import RegularHoliday
from .forms import HolidayCalendarForm, HolidayCalendarDeleteForm, HolidayCalendarUpdateForm
import datetime
import jpholiday
import calendar
from .serializer import HolidayCalendarSerializer

# from .serializer import CreditorSerializer,SupplierSerializer
# from .models import Creditor,Supplier
# from .forms import CreditorForm,CreditorUpdateForm,CreditorDeleteForm,SupplierForm,SupplierUpdateForm,SupplierDeleteForm


class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = "event_manager/calendar.html"

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '公民館ツール：日程管理'
        return context


class HolidayCalendarListView(LoginRequiredMixin, ListView):
    template_name = "event_manager/HolidayCalendar.html"
    success_url = reverse_lazy('event_manager:holiday')
    model = HolidayCalendar

    def get_queryset(self):
        today = datetime.date.today()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = HolidayCalendar.objects.filter(public_hall=current_public_hall).filter(
            date__year=today.year, public_hall=current_public_hall).order_by('date').all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        today = datetime.date.today()
        context = super().get_context_data()
        # page_title を追加する
        # context['object_list'] = HolidayCalendar.objects
        context['page_title'] = '休館日設定('+today.strftime('%Y')+'年)'
        context['form'] = HolidayCalendarForm()    # Create Modal画面
        context['form_update'] = HolidayCalendarUpdateForm()    # Update Modal画面
        context['form_delete'] = HolidayCalendarDeleteForm()    # Delete Modal画面
        return context

    def post(self, request):
        today = datetime.date.today()
        holidays = jpholiday.year_holidays(today.year)
        current_public_hall = self.request.user.public_hall
        for holiday in holidays:
            HolidayCalendar.objects.update_or_create(
                date=holiday[0], public_hall=current_public_hall,
                defaults={"name": holiday[1],
                          "public_hall": current_public_hall,
                          },
            )

        regularHoliday_list = RegularHoliday.objects.all()
        for regularHoliday in regularHoliday_list:
            for month in range(1, 13):
                weekday_count = 0
                _, end_day = calendar.monthrange(today.year, month)
                for day in range(1, end_day+1):
                    date = datetime.datetime(today.year, month, day)
                    if date.weekday() == int(regularHoliday.day_of_week):
                        weekday_count = weekday_count+1
                        if int(regularHoliday.semiweekly) == weekday_count or int(regularHoliday.day_of_week) == 0:
                            holiday, created = HolidayCalendar.objects.filter(date=date,public_hall=current_public_hall).get_or_create(date=date,name='休館日',public_hall=public_hall)
            
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarCreateView(LoginRequiredMixin,CreateView):
    model = HolidayCalendar
    form_class = HolidayCalendarForm
    success_url = reverse_lazy('event_manager:holidaycalendar')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarUpdateView(LoginRequiredMixin,UpdateView):
    model = HolidayCalendar
    form_class = HolidayCalendarUpdateForm
    success_url = reverse_lazy('event_manager:holidaycalendar')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalHolidayCalendarDeleteView(LoginRequiredMixin,DeleteView):
    model = HolidayCalendar
    success_url = reverse_lazy('event_manager:holidaycalendar')

class HolidayCalendarApiView(viewsets.ModelViewSet):
    queryset = HolidayCalendar.objects.all()
    serializer_class = HolidayCalendarSerializer