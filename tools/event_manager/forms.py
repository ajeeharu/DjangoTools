from .models import HolidayCalendar,UsageRecord,UserInformation
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

# 登録情報
class UsageRecordForm(forms.ModelForm):
    class Meta:
        model = UsageRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsageRecordForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class UsageRecordUpdateForm(UsageRecordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['id'] = "id_update_number"
        self.fields['user'].widget.attrs['id'] = "id_update_user"
        self.fields['details'].widget.attrs['id'] = "id_update_details"
        self.fields['application_date'].widget.attrs['id'] = "id_update_application_date"
        self.fields['date_of_use'].widget.attrs['id'] = "id_update_date_of_use"
        self.fields['start_time'].widget.attrs['id'] = "id_update_start_time"
        self.fields['end_time'].widget.attrs['id'] = "id_update_end_time"
        self.fields['number_of_users'].widget.attrs['id'] = "id_update_number_of_users"

        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"

class UsageRecordDeleteForm(UsageRecordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['date'].widget.attrs['id'] = "id_delete_date"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"

# 利用者情報
class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserInformationForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class UserInformationUpdateForm(UserInformationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['date'].widget.attrs['id'] = "id_update_date"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"

class UserInformationDeleteForm(UserInformationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['date'].widget.attrs['id'] = "id_delete_date"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"
