from .models import Creditor,Supplier
from django import forms

# 債権者情報
class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

class CreditorUpdateForm(CreditorForm):
    def __init__(self, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['address'].widget.attrs['id'] = "id_update_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class CreditorDeleteForm(CreditorForm):
    def __init__(self, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['address'].widget.attrs['id'] = "id_delete_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"

# 納入者情報
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"

class SupplierUpdateForm(SupplierForm):
    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['address'].widget.attrs['id'] = "id_update_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class SupplierDeleteForm(SupplierForm):
    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['address'].widget.attrs['id'] = "id_delete_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"
