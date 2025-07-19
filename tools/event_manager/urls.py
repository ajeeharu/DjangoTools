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

    path('usagerecord', views.UsageRecordListView.as_view(), name="usagerecord"),
    path('usagerecord/modal/create', views.ModalUsageRecordCreateView.as_view(), name="modal_create_usagerecord"),
    path('usagerecord/modal/<int:pk>/update', views.ModalUsageRecordUpdateView.as_view(), name="modal_update_usagerecord"),
    path('usagerecord/modal/<int:pk>/delete', views.ModalUsageRecordDeleteView.as_view(), name="modal_delete_usagerecord"),

	path('userinformation', views.UserInformationListView.as_view(), name="userinformation"),
    path('userinformation/modal/create', views.ModalUserInformationCreateView.as_view(), name="modal_create_userinformation"),
    path('userinformation/modal/<int:pk>/update', views.ModalUserInformationUpdateView.as_view(), name="modal_update_userinformation"),
    path('userinformation/modal/<int:pk>/delete', views.ModalUserInformationDeleteView.as_view(), name="modal_delete_userinformation"),

	path('room', views.RoomListView.as_view(), name="room"),
    path('room/modal/create', views.ModalRoomCreateView.as_view(), name="modal_create_room"),
    path('room/modal/<int:pk>/update', views.ModalRoomUpdateView.as_view(), name="modal_update_room"),
    path('room/modal/<int:pk>/delete', views.ModalRoomDeleteView.as_view(), name="modal_delete_room"),
]

router = DefaultRouter()
router.register('holidaycalendar', views.HolidayCalendarApiView,basename="holidaycalendar")
router.register('room', views.RoomApiView,basename="room")