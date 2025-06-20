from .models import HolidayCalendar
from django import forms


# 祝日情報
class HolidayCalendarForm(forms.ModelForm):
    class Meta:
        model = HolidayCalendar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HolidayCalendarForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class HolidayCalendarUpdateForm(HolidayCalendarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['date'].widget.attrs['id'] = "id_update_date"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"

class HolidayCalendarDeleteForm(HolidayCalendarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['date'].widget.attrs['id'] = "id_delete_date"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"
