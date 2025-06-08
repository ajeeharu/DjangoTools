from django.urls import path
from . import views

app_name = "event_manager"

urlpatterns = [
    path('', views.CalendarView.as_view(), name="calendar"),
    path('holiday', views.HolidayCalendarListView.as_view(), name="holiday"),
]

