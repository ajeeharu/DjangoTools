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

    path('fiscalterms', views.FiscalTermsListView.as_view(), name="fiscalterms"),
    path('fiscalterms/modal/create', views.ModalFiscalTermsCreateView.as_view(), name="modal_create_fiscalterms"),
    path('fiscalterms/modal/<int:pk>/update', views.ModalFiscalTermsUpdateView.as_view(), name="modal_update_fiscalterms"),
    path('fiscalterms/modal/<int:pk>/delete', views.ModalFiscalTermsDeleteView.as_view(), name="modal_delete_fiscalterms"),

    path('accountingbook', views.AccountingBookListView.as_view(), name="accountingbook"),
    path('accountingbook/modal/create', views.ModalAccountingBookCreateView.as_view(), name="modal_create_accountingbook"),
    path('accountingbook/modal/<int:pk>/update', views.ModalAccountingBookUpdateView.as_view(), name="modal_update_accountingbook"),
    path('accountingbook/modal/<int:pk>/delete', views.ModalAccountingBookDeleteView.as_view(), name="modal_delete_accountingbook"),

    path('subjectspending', views.SubjectSpendingListView.as_view(), name="subjectspending"),
    path('subjectspending/modal/create', views.ModalSubjectSpendingCreateView.as_view(), name="modal_create_subjectspending"),
    path('subjectspending/modal/<int:pk>/update', views.ModalSubjectSpendingUpdateView.as_view(), name="modal_update_subjectspending"),
    path('subjectspending/modal/<int:pk>/delete', views.ModalSubjectSpendingDeleteView.as_view(), name="modal_delete_subjectspending"),

    path('sectionspending', views.SectionSpendingListView.as_view(), name="sectionspending"),
    path('sectionspending/modal/create', views.ModalSectionSpendingCreateView.as_view(), name="modal_create_sectionspending"),
    path('sectionspending/modal/<int:pk>/update', views.ModalSectionSpendingUpdateView.as_view(), name="modal_update_sectionspending"),
    path('sectionspending/modal/<int:pk>/delete', views.ModalSectionSpendingDeleteView.as_view(), name="modal_delete_sectionspending"),

	path('subjectincome', views.SubjectIncomeListView.as_view(), name="subjectincome"),
    path('subjectincome/modal/create', views.ModalSubjectIncomeCreateView.as_view(), name="modal_create_subjectincome"),
    path('subjectincome/modal/<int:pk>/update', views.ModalSubjectIncomeUpdateView.as_view(), name="modal_update_subjectincome"),
    path('subjectincome/modal/<int:pk>/delete', views.ModalSubjectIncomeDeleteView.as_view(), name="modal_delete_subjectincome"),

    path('sectionincome', views.SectionIncomeListView.as_view(), name="sectionincome"),
    path('sectionincome/modal/create', views.ModalSectionIncomeCreateView.as_view(), name="modal_create_sectionincome"),
    path('sectionincome/modal/<int:pk>/update', views.ModalSectionIncomeUpdateView.as_view(), name="modal_update_sectionincome"),
    path('sectionincome/modal/<int:pk>/delete', views.ModalSectionIncomeDeleteView.as_view(), name="modal_delete_sectionincome"),

    path('incomerecord/create', views.IncomeRecordCreateView.as_view(), name="create_incomerecord"),
	path('incomerecord/<int:pk>/update', views.IncomeRecordUpdateView.as_view(), name="update_incomerecord"),
	path('incomerecord/<int:pk>/delete', views.IncomeRecordDeleteView.as_view(), name="delete_incomerecord"),

    path('spendingrecord/create', views.SpendingRecordCreateView.as_view(), name="create_spendingrecord"),
	path('spendingrecord/<int:pk>/update/<int:fiscal_terms>/<int:accounting_book>', views.SpendingRecordUpdateView.as_view(), name="update_spendingrecord"),
	path('spendingrecord/<int:pk>/delete', views.SpendingRecordDeleteView.as_view(), name="delete_spendingrecord"),

	path('response/<str:action>/<str:message>', views.ResponseMessage.as_view(), name="response_message"),
]

router = DefaultRouter()
router.register(r'creditor', views.CreditorApiView,basename="creditor")
router.register(r'supplier', views.SupplierApiView,basename="supplier")
router.register(r'fiscalterms', views.FiscalTermsApiView,basename="fiscalterms")
router.register(r'accountingbook', views.AccountingBookApiView,basename="accountingbook")
router.register(r'subjectspending', views.SubjectSpendingApiView,basename="subjectspending")
router.register(r'sectionspending', views.SectionSpendingApiView,basename="sectionspending")
router.register(r'subjectincome', views.SubjectIncomeApiView,basename="subjectincome")
router.register(r'sectionincome', views.SectionIncomeApiView,basename="sectionincome")

router.register(r'spendingrecord', views.SpendingRecordApiView,basename="spendingrecord")
router.register(r'incomerecord', views.IncomeRecordApiView,basename="incomerecord")
router.register(r'pagemanager', views.PageManagerApiView,basename="pagemanager")
