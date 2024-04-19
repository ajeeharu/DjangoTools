from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "login_user",
            "email",
            "name",
        )


# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User