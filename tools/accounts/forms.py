from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,PublicHall
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["login_user","email","name","public_hall","password"]

   #CustomUserに存在しないpassword2は追記
        password2 = forms.CharField(
            label='確認用パスワード',
            required=True,
            strip=False,
        )
        widgets = {
           'password': forms.PasswordInput(),
           'password2': forms.PasswordInput()
       }


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['public_hall'].queryset = PublicHall.objects.all()

        self.fields['login_user'].widget.attrs['class'] = self.fields['email'].widget.attrs['class']\
         = self.fields['public_hall'].widget.attrs['class'] = self.fields['password'].widget.attrs['class']\
         = self.fields['password2'].widget.attrs['class']\
         = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

        self.fields['login_user'].widget.attrs['placeholder'] = 'USER ID'
        self.fields['email'].widget.attrs['placeholder'] = 'xxx@yyy.zzz'
        self.fields['public_hall'].widget.attrs['required'] = True
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password2'].widget.attrs['placeholder'] = '確認用パスワード'

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("パスワードと確認用パスワードが合致しません")
        super().clean()

# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User
