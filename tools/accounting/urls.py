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

    path('supplier', views.SupplierListView.as_view(), name="supplier"),
    path('supplier/modal/create', views.ModalSupplierCreateView.as_view(), name="modal_create_supplier"),
    path('supplier/modal/<int:pk>/update', views.ModalSupplierUpdateView.as_view(), name="modal_update_supplier"),
    path('supplier/modal/<int:pk>/delete', views.ModalSupplierDeleteView.as_view(), name="modal_delete_supplier"),

]

router = DefaultRouter()
router.register(r'creditor', views.ModalCreditorApiView,basename="creditor")
router.register(r'supplier', views.ModalSupplierApiView,basename="supplier")