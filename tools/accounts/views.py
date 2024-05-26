from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom


class IndexView(TemplateView):
    # """ ホームビュー """
    # template_name = "index.html"
    form_class = LoginFrom
    template_name = "accounts/login.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        login_user = form.cleaned_data.get("login_user")
        password = form.cleaned_data.get("password1")
        user = authenticate(login_user=login_user, password=password)
        login(self.request, user)
        return response

class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

# LogoutViewを追加
class LogoutView(BaseLogoutView):
    template_name = "accounts/logout.html"
    # success_url = reverse_lazy("accounts:login")