from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "event_manager"

urlpatterns = [
    path('', views.CalendarView.as_view(), name="calendar"),
    path('holiday', views.HolidayCalendarListView.as_view(), name="holiday"),
    
    path('holidaycalendar', views.HolidayCalendarListView.as_view(), name="holidaycalendar"),
    path('holidaycalendar/modal/create', views.ModalHolidayCalendarCreateView.as_view(), name="modal_create_holidaycalendar"),
    path('holidaycalendar/modal/<int:pk>/update', views.ModalHolidayCalendarUpdateView.as_view(), name="modal_update_holidaycalendar"),
    path('holidaycalendar/modal/<int:pk>/delete', views.ModalHolidayCalendarDeleteView.as_view(), name="modal_delete_holidaycalendar"),
]

router = DefaultRouter()
router.register('holidaycalendar', views.HolidayCalendarApiView,basename="holidaycalendar")