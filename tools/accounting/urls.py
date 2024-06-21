from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "accounting"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('creditor', views.CreditorListView.as_view(), name="creditor"),
    path('creditor/modal/create', views.ModalCreditorCreateView.as_view(), name="modal_create_creditor"),
    path('creditor/modal/<int:pk>/update', views.ModalCreditorUpdateView.as_view(), name="modal_update_creditor"),
    path('creditor/modal/<int:pk>/delete', views.ModalCreditorDeleteView.as_view(), name="modal_delete_creditor"),
]

router = DefaultRouter()
router.register(r'creditor', views.ModalCreditorApiView,basename="creditor")