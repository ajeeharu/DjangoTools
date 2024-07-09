# coding: utf-8

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CreditorSerializer,SupplierSerializer,FiscalTermsSerializer,AccountingBookSerializer,SubjectSpendingSerializer,SectionSpendingSerializer,SubjectIncomeSerializer,SectionIncomeSerializer
from .models import Creditor,Supplier,PageManager,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,SubjectIncome,SectionIncome
from .forms import CreditorForm,CreditorUpdateForm,CreditorDeleteForm,SupplierForm,SupplierUpdateForm,SupplierDeleteForm,FiscalTermsForm,FiscalTermsUpdateForm,FiscalTermsDeleteForm, \
    AccountingBookForm,AccountingBookUpdateForm,AccountingBookDeleteForm,SubjectSpendingForm,SubjectSpendingUpdateForm,SubjectSpendingDeleteForm,SectionSpendingForm,SectionSpendingUpdateForm,SectionSpendingDeleteForm, \
    SubjectIncomeForm,SubjectIncomeUpdateForm,SubjectIncomeDeleteForm,SectionIncomeForm,SectionIncomeUpdateForm,SectionIncomeDeleteForm

class IndexView(LoginRequiredMixin,ListView):
    template_name = "accounting/index.html"
    model = PageManager

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = PageManager.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '出納帳'
        context['fiscal_term_objects'] = FiscalTerms.objects.all()
        context['accounting_book_objects'] = AccountingBook.objects.all()
        return context

# 債権者情報
class CreditorListView(LoginRequiredMixin,ListView):
    template_name = "accounting/creditor.html"
    model = Creditor

    def get_queryset(self):
        current_public_hall = self.request.user.public_hall # ログイン中の公民館を取得
        if current_public_hall:
            queryset = Creditor.objects.filter(public_hall=current_public_hall).all() # QuerySet（一致するレコード全て取得）
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

class ModalCreditorApiView(viewsets.ModelViewSet):
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

class ModalSupplierApiView(viewsets.ModelViewSet):
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

class ModalFiscalTermsApiView(viewsets.ModelViewSet):
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

class ModalAccountingBookApiView(viewsets.ModelViewSet):
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

class ModalSubjectSpendingApiView(viewsets.ModelViewSet):
    queryset = SubjectSpending.objects.all()
    serializer_class = SubjectSpendingSerializer

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

class ModalSectionSpendingApiView(viewsets.ModelViewSet):
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

class ModalSubjectIncomeApiView(viewsets.ModelViewSet):
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
    form_class = SectionIncomeUpdateForm
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

class ModalSectionIncomeApiView(viewsets.ModelViewSet):
    queryset = SectionIncome.objects.all()
    serializer_class = SectionIncomeSerializer

