from .models import RegularHoliday, UsageFee
from django import forms

# 定期休館日情報


class RegularHolidayForm(forms.ModelForm):
    class Meta:
        model = RegularHoliday
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RegularHolidayForm, self).__init__(*args, **kwargs)
        for i, n in enumerate(self.fields):
            self.fields[n].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"


class RegularHolidayUpdateForm(RegularHolidayForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day_of_week'].widget.attrs['id'] = "id_update_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_update_semiweekly"


class RegularHolidayDeleteForm(RegularHolidayForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, n in enumerate(self.fields):
            self.fields[n].widget.attrs['readonly'] = "readonly"
        self.fields['day_of_week'].widget.attrs['id'] = "id_delete_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_delete_semiweekly"

# 使用料設定


class UsageFeeForm(forms.ModelForm):
    class Meta:
        model = UsageFee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsageFeeForm, self).__init__(*args, **kwargs)
        for i, n in enumerate(self.fields):
            self.fields[n].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"
        self.fields['type'].widget.attrs['id'] = "id_update_type"
        self.fields['time_fee_1'].widget.attrs['id'] = "id_update_time_fee_1"
        self.fields['time_fee_2'].widget.attrs['id'] = "id_update_time_fee_2"
        self.fields['time_fee_3'].widget.attrs['id'] = "id_update_time_fee_3"
        self.fields['time_fee_1_with_air'].widget.attrs['id'] = "id_update_time_fee_1_with_air"
        self.fields['time_fee_2_with_air'].widget.attrs['id'] = "id_update_time_fee_2_with_air"
        self.fields['time_fee_3_with_air'].widget.attrs['id'] = "id_update_time_fee_3_with_air"
