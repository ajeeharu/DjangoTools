from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom # ログインフォームをimport


class IndexView(TemplateView):
    template_name = "accounts/login.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        # login after signup
        response = super().form_valid(form)
        login_user = form.cleaned_data.get("login_user")
        password = form.cleaned_data.get("password1")
        user = authenticate(login_user=login_user, password=password)
        login(self.request, user)
        return response

# ログイン
class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

# ログアウト
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")