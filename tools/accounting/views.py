# coding: utf-8

from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CreditorSerializer,SupplierSerializer,FiscalTermsSerializer,AccountingBookSerializer,SubjectSpendingSerializer,SectionSpendingSerializer,SubjectIncomeSerializer,SectionIncomeSerializer,SpendingRecordSerializer,IncomeRecordSerializer,PageManagerSerializer
from .models import Creditor,Supplier,PageManager,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,SubjectIncome,SectionIncome,IncomeRecord,PageManager,SpendingRecord,IncomeRecord
from .forms import CreditorForm,CreditorUpdateForm,CreditorDeleteForm,SupplierForm,SupplierUpdateForm,SupplierDeleteForm,FiscalTermsForm,FiscalTermsUpdateForm,FiscalTermsDeleteForm, \
    AccountingBookForm,AccountingBookUpdateForm,AccountingBookDeleteForm,SubjectSpendingForm,SubjectSpendingUpdateForm,SubjectSpendingDeleteForm,SectionSpendingForm,SectionSpendingUpdateForm,SectionSpendingDeleteForm, \
    SubjectIncomeForm,SubjectIncomeUpdateForm,SubjectIncomeDeleteForm,SectionIncomeForm,SectionIncomeUpdateForm,SectionIncomeDeleteForm,IncomeRecordForm,SpendingRecordForm,IncomeCreateFormset,SpendingCreateFormset

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.conf import settings
import openpyxl
import json

# 現金出納帳
class IndexView(LoginRequiredMixin,ListView):
    template_name = "accounting/index.html"
    model = PageManager
    success_url = reverse_lazy('accounting:index',kwargs={'fiscal_terms':0,'accounting_book':0})

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '現金出納帳'
        context['fiscal_term_objects'] = FiscalTerms.objects.all()
        context['accounting_book_objects'] = AccountingBook.objects.all()
        context['fiscal_terms'] = self.kwargs['fiscal_terms']
        context['accounting_book'] = self.kwargs['accounting_book']

        return context

    def form_valid(self, form):
        return

class IncomeRecordCreateView(LoginRequiredMixin,CreateView):
    # model = IncomeRecord
    form_class = IncomeRecordForm
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})
    template_name = "accounting/childwindow/income_record_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fiscal_terms = self.kwargs['fiscal_terms']
        accounting_book = self.kwargs['accounting_book']
        record_number = self.kwargs['record_number']
        public_hall = self.request.user.public_hall
        context['form_income_create'] = IncomeRecordForm()
        context['form_income_create'].fields['subject_income'].queryset = SubjectIncome.objects.filter(fiscal_terms=fiscal_terms, accounting_book=accounting_book,public_hall=public_hall)
        context['formset_income_page_create'] = IncomeCreateFormset()
        context['fiscal_terms'] = fiscal_terms
        context['accounting_book'] = accounting_book
        context['record_number'] = record_number
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            income_record =  form.save(commit=False)
            formset = IncomeCreateFormset(self.request.POST,instance=income_record)
            if formset.is_valid():
                return self.form_valid(form, formset )
        else:
            return self.form_invalid(form)

# データベースの処理終了後に子WIndowをClose
    def form_valid(self, form, formset):
        form.save()
        formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class IncomeRecordUpdateView(LoginRequiredMixin,UpdateView):
    model = IncomeRecord
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})
    template_name = "accounting/childwindow/income_record_update.html"
    form_class = IncomeRecordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fiscal_terms = self.kwargs['fiscal_terms']
        accounting_book = self.kwargs['accounting_book']
        public_hall = self.request.user.public_hall
        context['form'].fields['subject_income'].queryset = SubjectIncome.objects.filter(fiscal_terms=fiscal_terms, accounting_book=accounting_book,public_hall=public_hall)
        return context

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class IncomeRecordDeleteView(LoginRequiredMixin,DeleteView):
    model = IncomeRecord
    template_name = "accounting/childwindow/income_record_delete.html"
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[object] = IncomeRecord.objects.get(pk=self.kwargs['pk'])
        return context

class SpendingRecordCreateView(LoginRequiredMixin,CreateView):
    # model = SpendingRecord
    form_class = SpendingRecordForm
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})
    template_name = "accounting/childwindow/spending_record_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fiscal_terms = self.kwargs['fiscal_terms']
        accounting_book = self.kwargs['accounting_book']
        record_number = self.kwargs['record_number']
        public_hall = self.request.user.public_hall
        context['form_spending_create'] = SpendingRecordForm()
        context['form_spending_create'].fields['subject_spending'].queryset = SubjectSpending.objects.filter(fiscal_terms=fiscal_terms, accounting_book=accounting_book,public_hall=public_hall)
        context['formset_spending_page_create'] = SpendingCreateFormset()
        context['fiscal_terms'] = fiscal_terms
        context['accounting_book'] = accounting_book
        context['record_number'] = record_number
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            spending_record =  form.save(commit=False)
            formset = SpendingCreateFormset(self.request.POST,instance=spending_record)
            if formset.is_valid():
                return self.form_valid(form, formset )
        else:
            return self.form_invalid(form )

# データベースの処理終了後に子Window閉じる
    def form_valid(self, form, formset):
        print("forms_valid")
        form.save()
        formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        print("form_invalid")
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class SpendingRecordUpdateView(LoginRequiredMixin,UpdateView):
    model = SpendingRecord
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})
    template_name = "accounting/childwindow/spending_record_update.html"
    form_class = SpendingRecordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fiscal_terms = self.kwargs['fiscal_terms']
        accounting_book = self.kwargs['accounting_book']
        public_hall = self.request.user.public_hall
        context['form'].fields['subject_spending'].queryset = SubjectSpending.objects.filter(fiscal_terms=fiscal_terms, accounting_book=accounting_book,public_hall=public_hall)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

# ここではcontextのデータをセットするだけ
# Delete処理はRestFul APIで行う。
# 理由：Delete後に同じURLに戻ろうとすると、該当PKが削除されているので該当データなしのエラーとなる。
class SpendingRecordDeleteView(LoginRequiredMixin,DeleteView):
    model = SpendingRecord
    template_name = "accounting/childwindow/spending_record_delete.html"
    success_url = reverse_lazy('accounting:response_message',kwargs={'action':'CloseChildWindow','message':'OK'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[object] = SpendingRecord.objects.get(pk=self.kwargs['pk'])
        return context


class SpendingRecordApiView(viewsets.ModelViewSet):
    queryset = SpendingRecord.objects.all()
    serializer_class = SpendingRecordSerializer

    def patch(self, request, pk, *args, **kwargs):
        # instanceの取得
        instance = get_object_or_404(SpendingRecord, pk=pk)
        serializer = SpendingRecordSerializer(instance=instance, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # DB更新
        serializer.save()
        return Response({'result':True})

class IncomeRecordApiView(viewsets.ModelViewSet):
    queryset = IncomeRecord.objects.all()
    serializer_class = IncomeRecordSerializer

    def patch(self, request, pk, *args, **kwargs):
        # instanceの取得
        instance = get_object_or_404(IncomeRecord, pk=pk)
        serializer = IncomeRecordSerializer(instance=instance, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # DB更新
        serializer.save()
        return Response({'result':True})

class PageManagerApiView(viewsets.ModelViewSet):
    serializer_class = PageManagerSerializer

    def get_queryset(self):
        queryset = PageManager.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        if self.request.query_params.get('fiscal_terms'):
            queryset = queryset.filter(fiscal_terms=self.request.query_params.get('fiscal_terms'))       # QuerySet（期間指定が一致）
        if self.request.query_params.get('accounting_book'):
            queryset = queryset.filter(accounting_book=self.request.query_params.get('accounting_book'))   # QuerySet（出納帳が一致）
        queryset = queryset.order_by('number')                                 # シリアル番号順

        return queryset

    def patch(self, request, pk, *args, **kwargs):
        # instanceの取得
        instance = get_object_or_404(PageManager, pk=pk)
        serializer = PageManagerSerializer(instance=instance, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # DB更新
        serializer.save()
        return Response({'result':True})

# 債権者情報
class CreditorListView(LoginRequiredMixin,ListView):
    template_name = "accounting/creditor.html"
    model = Creditor

    def get_queryset(self):
        queryset = Creditor.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)     # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '債権者情報'
        context['form'] = CreditorForm()    # Create Modal画面
        context['form_update'] = CreditorUpdateForm()    # Update Modal画面
        context['form_delete'] = CreditorDeleteForm()    # Delete Modal画面
        return context

class ModalCreditorCreateView(LoginRequiredMixin,CreateView):
    model = Creditor
    form_class = CreditorForm
    success_url = reverse_lazy('accounting:creditor')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalCreditorUpdateView(LoginRequiredMixin,UpdateView):
    model = Creditor
    form_class = CreditorUpdateForm
    success_url = reverse_lazy('accounting:creditor')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalCreditorDeleteView(LoginRequiredMixin,DeleteView):
    model = Creditor
    success_url = reverse_lazy('accounting:creditor')

class CreditorApiView(viewsets.ModelViewSet):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer

# 納入者情報
class SupplierListView(CreditorListView):
    template_name = "accounting/supplier.html"
    model = Supplier

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = Supplier.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '納入者情報'
        context['form'] = SupplierForm()    # Create/Update Modal画面用
        context['form_update'] = SupplierUpdateForm()    # Create/Update Modal画面用
        context['form_delete'] = SupplierDeleteForm()    # Create/Update Modal画面用
        return context

class ModalSupplierCreateView(LoginRequiredMixin,CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('accounting:supplier')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSupplierUpdateView(LoginRequiredMixin,UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm
    success_url = reverse_lazy('accounting:supplier')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSupplierDeleteView(LoginRequiredMixin,DeleteView):
    model = Supplier
    success_url = reverse_lazy('accounting:supplier')

class SupplierApiView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# 会計年度情報
class FiscalTermsListView(LoginRequiredMixin,ListView):
    template_name = "accounting/fiscalterms.html"
    model = FiscalTerms

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '会計年度情報'
        context['form'] = FiscalTermsForm()    # Create Modal画面
        context['form_update'] = FiscalTermsUpdateForm()    # Update Modal画面
        context['form_delete'] = FiscalTermsDeleteForm()    # Delete Modal画面
        return context

class ModalFiscalTermsCreateView(LoginRequiredMixin,CreateView):
    model = FiscalTerms
    form_class = FiscalTermsForm
    success_url = reverse_lazy('accounting:fiscalterms')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalFiscalTermsUpdateView(LoginRequiredMixin,UpdateView):
    model = FiscalTerms
    form_class = FiscalTermsUpdateForm
    success_url = reverse_lazy('accounting:fiscalterms')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalFiscalTermsDeleteView(LoginRequiredMixin,DeleteView):
    model = FiscalTerms
    success_url = reverse_lazy('accounting:fiscalterms')

class FiscalTermsApiView(viewsets.ModelViewSet):
    queryset = FiscalTerms.objects.all()
    serializer_class = FiscalTermsSerializer

# 出納帳情報
class AccountingBookListView(LoginRequiredMixin,ListView):
    template_name = "accounting/accountingbook.html"
    model = AccountingBook

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '出納帳情報'
        context['form'] = AccountingBookForm()    # Create Modal画面
        context['form_update'] = AccountingBookUpdateForm()    # Update Modal画面
        context['form_delete'] = AccountingBookDeleteForm()    # Delete Modal画面
        return context

class ModalAccountingBookCreateView(LoginRequiredMixin,CreateView):
    model = AccountingBook
    form_class = AccountingBookForm
    success_url = reverse_lazy('accounting:accountingbook')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalAccountingBookUpdateView(LoginRequiredMixin,UpdateView):
    model = AccountingBook
    form_class = AccountingBookUpdateForm
    success_url = reverse_lazy('accounting:accountingbook')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalAccountingBookDeleteView(LoginRequiredMixin,DeleteView):
    model = AccountingBook
    success_url = reverse_lazy('accounting:accountingbook')

class AccountingBookApiView(viewsets.ModelViewSet):
    queryset = AccountingBook.objects.all()
    serializer_class = AccountingBookSerializer

# 科目(支出）情報
class SubjectSpendingListView(LoginRequiredMixin,ListView):
    template_name = "accounting/subjectspending.html"
    model = SubjectSpending

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = SubjectSpending.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '科目(支出）情報'
        context['form'] = SubjectSpendingForm()    # Create Modal画面
        context['form_update'] = SubjectSpendingUpdateForm()    # Update Modal画面
        context['form_delete'] = SubjectSpendingDeleteForm()    # Delete Modal画面
        return context

class ModalSubjectSpendingCreateView(LoginRequiredMixin,CreateView):
    model = SubjectSpending
    form_class = SubjectSpendingForm
    success_url = reverse_lazy('accounting:subjectspending')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSubjectSpendingUpdateView(LoginRequiredMixin,UpdateView):
    model = SubjectSpending
    form_class = SubjectSpendingUpdateForm
    success_url = reverse_lazy('accounting:subjectspending')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSubjectSpendingDeleteView(LoginRequiredMixin,DeleteView):
    model = SubjectSpending
    success_url = reverse_lazy('accounting:subjectspending')

class SubjectSpendingApiView(viewsets.ModelViewSet):
    serializer_class = SubjectSpendingSerializer

    def get_queryset(self):
        queryset = SubjectSpending.objects.all()
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = queryset.filter(public_hall=current_public_hall)         # QuerySet（ログインしている公民館）
        current_fiscal_terms = self.request.query_params.get('fiscal_terms')
        if current_fiscal_terms is not None:
            queryset = queryset.filter(fiscal_terms=current_fiscal_terms)       # QuerySet（期間指定が一致）
        current_accounting_book = self.request.query_params.get('accounting_book')
        if current_accounting_book is not None:
            queryset = queryset.filter(accounting_book=current_accounting_book)   # QuerySet（出納帳が一致）
        return queryset

# 節（支出）情報
class SectionSpendingListView(LoginRequiredMixin,ListView):
    template_name = "accounting/sectionspending.html"
    model = SectionSpending

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '節（支出）情報'
        context['form'] = SectionSpendingForm()    # Create Modal画面
        context['form_update'] = SectionSpendingUpdateForm()    # Update Modal画面
        context['form_delete'] = SectionSpendingDeleteForm()    # Delete Modal画面
        return context

class ModalSectionSpendingCreateView(LoginRequiredMixin,CreateView):
    model = SectionSpending
    form_class = SectionSpendingForm
    success_url = reverse_lazy('accounting:sectionspending')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSectionSpendingUpdateView(LoginRequiredMixin,UpdateView):
    model = SectionSpending
    form_class = SectionSpendingUpdateForm
    success_url = reverse_lazy('accounting:sectionspending')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSectionSpendingDeleteView(LoginRequiredMixin,DeleteView):
    model = SectionSpending
    success_url = reverse_lazy('accounting:sectionspending')

class SectionSpendingApiView(viewsets.ModelViewSet):
    queryset = SectionSpending.objects.all()
    serializer_class = SectionSpendingSerializer

# 科目（収入）情報
class SubjectIncomeListView(LoginRequiredMixin,ListView):
    template_name = "accounting/subjectincome.html"
    model = SubjectIncome

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = SubjectIncome.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '科目（収入）情報'
        context['form'] = SubjectIncomeForm()    # Create Modal画面
        context['form_update'] = SubjectIncomeUpdateForm()    # Update Modal画面
        context['form_delete'] = SubjectIncomeDeleteForm()    # Delete Modal画面
        return context

class ModalSubjectIncomeCreateView(LoginRequiredMixin,CreateView):
    model = SubjectIncome
    form_class = SubjectIncomeForm
    success_url = reverse_lazy('accounting:subjectincome')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSubjectIncomeUpdateView(LoginRequiredMixin,UpdateView):
    model = SubjectIncome
    form_class = SubjectIncomeUpdateForm
    success_url = reverse_lazy('accounting:subjectincome')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSubjectIncomeDeleteView(LoginRequiredMixin,DeleteView):
    model = SubjectIncome
    success_url = reverse_lazy('accounting:subjectincome')

class SubjectIncomeApiView(viewsets.ModelViewSet):
    queryset = SubjectIncome.objects.all()
    serializer_class = SubjectIncomeSerializer

# 節（収入）情報
class SectionIncomeListView(LoginRequiredMixin,ListView):
    template_name = "accounting/sectionincome.html"
    model = SectionIncome

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '節（収入）情報'
        context['form'] = SectionIncomeForm()    # Create Modal画面
        context['form_update'] = SectionIncomeUpdateForm()    # Update Modal画面
        context['form_delete'] = SectionIncomeDeleteForm()    # Delete Modal画面
        return context

class ModalSectionIncomeCreateView(LoginRequiredMixin,CreateView):
    model = SectionIncome
    form_class = SectionIncomeForm
    success_url = reverse_lazy('accounting:sectionincome')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSectionIncomeUpdateView(LoginRequiredMixin,UpdateView):
    model = SectionIncome
    form_class = SubjectIncomeUpdateForm
    success_url = reverse_lazy('accounting:sectionincome')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalSectionIncomeDeleteView(LoginRequiredMixin,DeleteView):
    model = SectionIncome
    success_url = reverse_lazy('accounting:sectionincome')

class SectionIncomeApiView(viewsets.ModelViewSet):
    queryset = SectionIncome.objects.all()
    serializer_class = SectionIncomeSerializer

# メッセージ通知用（例：
class ResponseMessage(LoginRequiredMixin,TemplateView):
    template_name = "accounting/response.html"


class ExportView(LoginRequiredMixin,ListView):
    template_name = "accounting/export.html"
    model = PageManager

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = 'EXPORT'
        fiscal_terms = self.kwargs['fiscal_terms']
        accounting_book = self.kwargs['accounting_book']
        context['fiscal_terms'] = fiscal_terms
        context['accounting_book'] = accounting_book
        context['fiscal_terms_name'] = FiscalTerms.objects.get(pk=fiscal_terms).name
        context['accounting_book_name'] = AccountingBook.objects.get(pk=accounting_book).name

        return context


# 現金出納帳、支出伝票、収入伝票をEXCELでダウンロード
def DownloadExcel(request):
    data = json.loads(request.body)
    for row in data:
        print(row)
    wb =openpyxl.load_workbook(settings.MEDIA_ROOT + '/excel/template_accounting.xlsx')
    ws = wb.active
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'template.xlsx'
    wb.save(response)
    return response