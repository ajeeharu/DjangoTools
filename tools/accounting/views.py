# coding: utf-8

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CreditorSerializer
from .models import Creditor
from .forms import CreditorForm




class IndexView(LoginRequiredMixin,TemplateView):
    """ ホームビュー """
    template_name = "accounting/index.html"

# 債権者情報
class CreditorListView(LoginRequiredMixin,ListView):
    template_name = "accounting/creditor.html"
    model = Creditor
    # ordering = 'number'

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '債権者情報一覧'
        context['form'] = CreditorForm()    # Create/Update Modal画面用
        return context

# 一覧表示からのModalWwindowで表示
class CreditorCreateView(LoginRequiredMixin,CreateView):
    form_class = Creditor
    success_url = reverse_lazy('accounting:creditor')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class CreditorUpdateView(LoginRequiredMixin,UpdateView):
    model = Creditor
    form_class = CreditorForm
    success_url = reverse_lazy('accounting:creditor')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class CreditorDeleteView(LoginRequiredMixin,DeleteView):
    model = Creditor
    success_url = reverse_lazy('accounting:creditor')

class CreditorApiView(viewsets.ModelViewSet):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer