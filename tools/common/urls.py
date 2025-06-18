from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "common"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('settings', views.SettingsView.as_view(), name="settings"),
    
    path('regularholiday', views.RegularHolidayListView.as_view(), name="regularholiday"),
    path('regularholiday/modal/create', views.ModalRegularHolidayCreateView.as_view(), name="modal_create_regularholiday"),
    path('regularholiday/modal/<int:pk>/update', views.ModalRegularHolidayUpdateView.as_view(), name="modal_update_regularholiday"),
    path('regularholiday/modal/<int:pk>/delete', views.ModalRegularHolidayDeleteView.as_view(), name="modal_delete_regularholiday"),
]

router = DefaultRouter()
router.register('regularholiday', views.RegularHolidayApiView,basename="regularholiday")