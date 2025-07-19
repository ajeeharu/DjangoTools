# coding: utf-8

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .models import HolidayCalendar,UsageRecord,UserInformation,Room
from common.models import RegularHoliday,UsageFee
from .forms import HolidayCalendarForm, HolidayCalendarDeleteForm, HolidayCalendarUpdateForm, UsageRecordForm, UsageRecordUpdateForm, UsageRecordDeleteForm, UserInformationForm, UserInformationUpdateForm, UserInformationDeleteForm, RoomForm, RoomDeleteForm, RoomUpdateForm
import datetime
import jpholiday
import calendar
from .serializer import HolidayCalendarSerializer,UsageRecordSerializer,UserInformationSerializer,RoomSerializer


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
    serializer_class = HolidayCalendarSerializer
    
    def get_queryset(self):
        queryset = HolidayCalendar.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        current_year = self.request.query_params.get('year')
        if current_year is not None:
            queryset = queryset.filter(date__year=current_year)       # QuerySet（期間指定が一致）
        return queryset

#イベント登録
class UsageRecordListView(LoginRequiredMixin,ListView):
    template_name = "event_manager/usagerecord.html"
    model = UsageRecord

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = UsageRecord.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = 'イベント登録'
        context['form'] = UsageRecordForm()    # Create Modal画面
        context['form_update'] = UsageRecordUpdateForm()    # Update Modal画面
        context['form_delete'] = UsageRecordDeleteForm()    # Delete Modal画面
        return context

class ModalUsageRecordCreateView(LoginRequiredMixin,CreateView):
    model = UsageRecord
    form_class = UsageRecordForm
    success_url = reverse_lazy('event_manager:usagerecord')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalUsageRecordUpdateView(LoginRequiredMixin,UpdateView):
    model = UsageRecord
    form_class = UsageRecordUpdateForm
    success_url = reverse_lazy('event_manager:usagerecord')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalUsageRecordDeleteView(LoginRequiredMixin,DeleteView):
    model = UsageRecord
    success_url = reverse_lazy('event_manager:usagerecord')

class UsageRecordApiView(viewsets.ModelViewSet):
    serializer_class = UsageRecordSerializer

    def get_queryset(self):
        queryset = UsageRecord.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        current_fiscal_terms = self.request.query_params.get('fiscal_terms')
        if current_fiscal_terms is not None:
            queryset = queryset.filter(fiscal_terms=current_fiscal_terms)       # QuerySet（期間指定が一致）
        current_event_manager_book = self.request.query_params.get('event_manager_book')
        if current_event_manager_book is not None:
            queryset = queryset.filter(event_manager_book=current_event_manager_book)   # QuerySet（出納帳が一致）
        return queryset

# 利用者情報
class UserInformationListView(LoginRequiredMixin,ListView):
    template_name = "event_manager/userinformation.html"
    model = UserInformation

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = UserInformation.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '利用者情報'
        context['form'] = UserInformationForm()    # Create Modal画面
        context['form_update'] = UserInformationUpdateForm()    # Update Modal画面
        context['form_delete'] = UserInformationDeleteForm()    # Delete Modal画面
        return context

class ModalUserInformationCreateView(LoginRequiredMixin,CreateView):
    model = UserInformation
    form_class = UserInformationForm
    success_url = reverse_lazy('event_manager:userinformation')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalUserInformationUpdateView(LoginRequiredMixin,UpdateView):
    model = UserInformation
    form_class = UserInformationUpdateForm
    success_url = reverse_lazy('event_manager:userinformation')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalUserInformationDeleteView(LoginRequiredMixin,DeleteView):
    model = UserInformation
    success_url = reverse_lazy('event_manager:userinformation')

class UserInformationApiView(viewsets.ModelViewSet):
    serializer_class = UserInformationSerializer

    def get_queryset(self):
        queryset = UserInformation.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        return queryset

#公民館の施設情報
class RoomListView(LoginRequiredMixin,ListView):
    template_name = "event_manager/room.html"
    model = Room

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = Room.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '公民館施設登録'
        context['form'] = RoomForm()    # Create Modal画面
        context['form_update'] = RoomUpdateForm()    # Update Modal画面
        context['form_delete'] = RoomDeleteForm()    # Delete Modal画面
        return context

class ModalRoomCreateView(LoginRequiredMixin,CreateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('event_manager:room')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalRoomUpdateView(LoginRequiredMixin,UpdateView):
    model = Room
    form_class = RoomUpdateForm
    success_url = reverse_lazy('event_manager:room')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalRoomDeleteView(LoginRequiredMixin,DeleteView):
    model = Room
    success_url = reverse_lazy('event_manager:room')

class RoomApiView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        return queryset
