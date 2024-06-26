from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,PublicHall
from django import forms

# ユーザー登録
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["login_user","email","name","public_hall","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['public_hall'].queryset = PublicHall.objects.all()

        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

        self.fields['login_user'].widget.attrs['placeholder'] = 'USER ID'
        self.fields['email'].widget.attrs['placeholder'] = 'xxx@yyy.zzz'
        self.fields['name'].widget.attrs['placeholder'] = '清水　すげ'
        self.fields['public_hall'].widget.attrs['required'] = True
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password2'].widget.attrs['placeholder'] = '確認用パスワード'


# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User

# 公民館情報
class HallForm(forms.ModelForm):
    class Meta:
        model = PublicHall
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HallForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

        self.fields['name'].widget.attrs['placeholder'] = '例：清水南'
        self.fields['email'].widget.attrs['placeholder'] = 'xxx@yyy.zzz'
        self.fields['tel'].widget.attrs['placeholder'] = '0776-99-9999'
