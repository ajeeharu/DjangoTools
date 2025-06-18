from .models import RegularHoliday
from django import forms

# 定期休館日情報
class RegularHolidayForm(forms.ModelForm):
    class Meta:
        model = RegularHoliday
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RegularHolidayForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class RegularHolidayUpdateForm(RegularHolidayForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day_of_week'].widget.attrs['id'] = "id_update_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_update_semiweekly"


class RegularHolidayDeleteForm(RegularHolidayForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['day_of_week'].widget.attrs['id'] = "id_delete_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_delete_semiweekly"
