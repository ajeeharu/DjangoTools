from .models import HolidayCalendar,UsageRecord,UserInformation,Room
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
        self.fields['number'].widget.attrs['id'] = "id_delete_number"
        self.fields['user'].widget.attrs['id'] = "id_delete_user"
        self.fields['details'].widget.attrs['id'] = "id_delete_details"
        self.fields['application_date'].widget.attrs['id'] = "id_delete_application_date"
        self.fields['date_of_use'].widget.attrs['id'] = "id_delete_date_of_use"
        self.fields['start_time'].widget.attrs['id'] = "id_delete_start_time"
        self.fields['end_time'].widget.attrs['id'] = "id_delete_end_time"
        self.fields['number_of_users'].widget.attrs['id'] = "id_delete_number_of_users"

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
        self.fields['organization_name'].widget.attrs['id'] = "id_update_organization_name"
        self.fields['usage_category'].widget.attrs['id'] = "id_update_usage_category"
        self.fields['educational_category'].widget.attrs['id'] = "id_update_educational_category"
        self.fields['day_of_week'].widget.attrs['id'] = "id_update_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_update_semiweekly"
        self.fields['responsible_party'].widget.attrs['id'] = "id_update_responsible_party"
        self.fields['address'].widget.attrs['id'] = "id_update_address"
        self.fields['tel'].widget.attrs['id'] = "id_update_tel"
        self.fields['default_start_time'].widget.attrs['id'] = "id_update_default_start_time"
        self.fields['default_end_time'].widget.attrs['id'] = "id_update_default_end_time"
        self.fields['default_room'].widget.attrs['id'] = "id_update_default_room"
        self.fields['default_remarks'].widget.attrs['id'] = "id_update_default_remarks"
        self.fields['default_details'].widget.attrs['id'] = "id_update_default_details"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"

class UserInformationDeleteForm(UserInformationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['organization_name'].widget.attrs['id'] = "id_delete_organization_name"
        self.fields['usage_category'].widget.attrs['id'] = "id_delete_usage_category"
        self.fields['educational_category'].widget.attrs['id'] = "id_delete_educational_category"
        self.fields['day_of_week'].widget.attrs['id'] = "id_delete_day_of_week"
        self.fields['semiweekly'].widget.attrs['id'] = "id_delete_semiweekly"
        self.fields['responsible_party'].widget.attrs['id'] = "id_delete_responsible_party"
        self.fields['address'].widget.attrs['id'] = "id_delete_address"
        self.fields['tel'].widget.attrs['id'] = "id_delete_tel"
        self.fields['default_start_time'].widget.attrs['id'] = "id_delete_default_start_time"
        self.fields['default_end_time'].widget.attrs['id'] = "id_delete_default_end_time"
        self.fields['default_room'].widget.attrs['id'] = "id_delete_default_room"
        self.fields['default_remarks'].widget.attrs['id'] = "id_delete_default_remarks"
        self.fields['default_details'].widget.attrs['id'] = "id_delete_default_details"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"

# 公民館施設情報
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class RoomUpdateForm(RoomForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['type'].widget.attrs['id'] = "id_update_type"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"

class RoomDeleteForm(RoomForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_dalete_name"
        self.fields['type'].widget.attrs['id'] = "id_delete_type"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"
