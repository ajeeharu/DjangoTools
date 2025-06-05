from django.urls import path
from . import views

app_name = "event_manager"

urlpatterns = [
    path('', views.CalendarView.as_view(), name="calendar"),
    path('2', views.Calendar2View.as_view(), name="calendar2"),
]

