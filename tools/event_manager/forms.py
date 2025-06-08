from .models import HolidayCalendar
from django import forms


# 祝日情報
class HolidayCalendarForm(forms.ModelForm):
    class Meta:
        model = HolidayCalendar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HolidayCalendarForm, self).__init__(*args, **kwargs)
        # for i ,n in enumerate( self.fields ):
        #     self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"
        # self.fields['start_date'].widget.attrs['placeholder'] = '2024/4/1'
        # self.fields['end_date'].widget.attrs['placeholder'] = '2025/3/31'

class HolidayCalendarUpdateForm(HolidayCalendarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['id'] = "id_update_name"
        # self.fields['start_date'].widget.attrs['id'] = "id_update_start_date"
        # self.fields['end_date'].widget.attrs['id'] = "id_update_end_date"


class HolidayCalendarDeleteForm(HolidayCalendarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for i ,n in enumerate( self.fields ):
        #     self.fields[ n ].widget.attrs['readonly'] = "readonly"
        # self.fields['name'].widget.attrs['id'] = "id_delete_name"
        # self.fields['start_date'].widget.attrs['id'] = "id_delete_start_date"
        # self.fields['end_date'].widget.attrs['id'] = "id_delete_end_date"
