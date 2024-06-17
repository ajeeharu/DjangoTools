from .models import Creditor
from django import forms

# 公民館情報
class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] = self.fields['email'].widget.attrs['class']\
         = self.fields['tel'].widget.attrs['class'] = self.fields['name'].widget.attrs['class']\
         = self.fields['director'].widget.attrs['class'] \
         = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

        self.fields['name'].widget.attrs['placeholder'] = '例：清水南'
        self.fields['email'].widget.attrs['placeholder'] = 'xxx@yyy.zzz'
        self.fields['tel'].widget.attrs['placeholder'] = '0776-99-9999'
