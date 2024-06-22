# coding: utf-8

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CreditorSerializer,SupplierSerializer
from .models import Creditor,Supplier
from .forms import CreditorForm,CreditorUpdateForm,CreditorDeleteForm,SupplierForm,SupplierUpdateForm,SupplierDeleteForm



class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "accounting/index.html"

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
