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
        current_public_hall = self.request.user.public_hall  # ログイン中の公民館を取得
        if current_public_hall:
            queryset = HolidayCalendar.objects.filter(public_hall=current_public_hall).filter(
                # QuerySet（一致するレコード全て取得）
                date__year=today.year, public_hall=current_public_hall).order_by('date').all()
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
        current_year = datetime.date.today().year
        current_public_hall = self.request.user.public_hall
# 該当(年度、所属公民館）するデータを削除
        # print('delete')
        HolidayCalendar.objects.filter(
            date__year=current_year, public_hall=current_public_hall).delete()
# 祝日データを取得
        # print('holiday update_or_create')
        holidays = jpholiday.year_holidays(current_year)
        for holiday in holidays:
            HolidayCalendar.objects.update_or_create(
                date=holiday[0], public_hall=current_public_hall,
                defaults={"name": holiday[1]},
            )
# 定休日を設定
        # print('regular holiday update_or_create')
        regularHoliday_list = RegularHoliday.objects.all()
        for regularHoliday in regularHoliday_list:
            for month in range(1, 13):
                weekday_count = 1
                _, end_day = calendar.monthrange(current_year, month)
                for day in range(1, end_day+1):
                    date = datetime.datetime(current_year, month, day)
                    if date.weekday() == int(regularHoliday.day_of_week):
                        if int(regularHoliday.semiweekly) == weekday_count or int(regularHoliday.day_of_week) == 0:
                            try:
                                holiday = HolidayCalendar.objects.filter(
                                    date=date, public_hall=current_public_hall).get()
                                # 祝日の振替か確認する。
                                if (holiday.name.find('振替') == (-1)):
                                    # print('振替')
                                    date = datetime.datetime(
                                        current_year, month, day+1)
                                    # 翌日が祝日でなければ振替休館日にする
                                    try:
                                        holiday = HolidayCalendar.objects.filter(
                                          date=date, public_hall=current_public_hall).get()
                                    except HolidayCalendar.DoesNotExist:
                                        HolidayCalendar.objects.create(
                                           date=date, name='振替休館日', public_hall=current_public_hall)
                            except HolidayCalendar.DoesNotExist:
                                # print('休館日')
                                HolidayCalendar.objects.create(
                                    date=date, name='休館日', public_hall=current_public_hall)
                        weekday_count = weekday_count+1

        return HttpResponseRedirect(self.success_url)


class ModalHolidayCalendarCreateView(LoginRequiredMixin, CreateView):
    model = HolidayCalendar
    form_class = HolidayCalendarForm
    success_url = reverse_lazy('event_manager:holidaycalendar')

    def form_valid(self, form):
        form.save()  # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)


class ModalHolidayCalendarUpdateView(LoginRequiredMixin, UpdateView):
    model = HolidayCalendar
    form_class = HolidayCalendarUpdateForm
    success_url = reverse_lazy('event_manager:holidaycalendar')

    def form_valid(self, form):
        form.save()  # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)


class ModalHolidayCalendarDeleteView(LoginRequiredMixin, DeleteView):
    model = HolidayCalendar
    success_url = reverse_lazy('event_manager:holidaycalendar')


class HolidayCalendarApiView(viewsets.ModelViewSet):
    queryset = HolidayCalendar.objects.all()
    serializer_class = HolidayCalendarSerializer
