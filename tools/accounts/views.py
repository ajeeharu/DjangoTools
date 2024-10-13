from django.contrib.auth import login
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom, HallForm
from django.http import HttpResponseRedirect
from .models import PublicHall
from django.contrib import messages
from rest_framework import viewsets
from .serializer import PublicHallSerializer

class IndexView(TemplateView):
    # """ ホームビュー """
    # template_name = "index.html"
    form_class = LoginFrom
    template_name = "accounts/login.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('accounting:index',kwargs={'fiscal_terms':0,'accounting_book':0}) # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

# LogoutViewを追加
class LogoutView(BaseLogoutView):
    template_name = "accounts/logout.html"

# 公民館情報
class HallListView(ListView):
    template_name = "accounts/public_hall.html"
    model = PublicHall
    ordering = 'number'

    def get_context_data(self):
        context = super().get_context_data()
        # page_title を追加する
        context['page_title'] = '公民館情報一覧'
        context['form'] = HallForm()    # Create/Update Modal画面用
        return context

# 一覧表示からのModalWwindowで表示
class ModalHallCreateView(CreateView):
    form_class = HallForm
    success_url = reverse_lazy('accounts:hall')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)


class ModalHallUpdateView(UpdateView):
    model = PublicHall
    form_class = HallForm
    success_url = reverse_lazy('accounts:hall')

    def form_valid(self, form):
        form.save() # formの情報を保存
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors)
        return HttpResponseRedirect(self.success_url)

class ModalHallDeleteView(DeleteView):
    model = PublicHall
    success_url = reverse_lazy('accounts:hall')

class ModalHallApiView(viewsets.ModelViewSet):
    queryset = PublicHall.objects.all()
    serializer_class = PublicHallSerializer