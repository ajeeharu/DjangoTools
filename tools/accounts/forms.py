from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "login_user",
            "email",
            "public_hall",
        )

class LoginFrom(AuthenticationForm):
    class Meta:
        model = User