from .models import Creditor,Supplier,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,SubjectIncome,SectionIncome,IncomeRecord,SpendingRecord,PageManager
from django import forms

# 債権者情報
class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class CreditorUpdateForm(CreditorForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['address'].widget.attrs['id'] = "id_update_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class CreditorDeleteForm(CreditorForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
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
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class SupplierUpdateForm(SupplierForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['address'].widget.attrs['id'] = "id_update_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class SupplierDeleteForm(SupplierForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['address'].widget.attrs['id'] = "id_delete_address"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"

# 会計年度情報
class FiscalTermsForm(forms.ModelForm):
    class Meta:
        model = FiscalTerms
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FiscalTermsForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"
        self.fields['start_date'].widget.attrs['placeholder'] = '2024/4/1'
        self.fields['end_date'].widget.attrs['placeholder'] = '2025/3/31'

class FiscalTermsUpdateForm(FiscalTermsForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['start_date'].widget.attrs['id'] = "id_update_start_date"
        self.fields['end_date'].widget.attrs['id'] = "id_update_end_date"


class FiscalTermsDeleteForm(FiscalTermsForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['start_date'].widget.attrs['id'] = "id_delete_start_date"
        self.fields['end_date'].widget.attrs['id'] = "id_delete_end_date"

# 出納帳情報
class AccountingBookForm(forms.ModelForm):
    class Meta:
        model = AccountingBook
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AccountingBookForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class AccountingBookUpdateForm(AccountingBookForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"


class AccountingBookDeleteForm(AccountingBookForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"


# 科目（支出）情報
class SubjectSpendingForm(forms.ModelForm):
    class Meta:
        model = SubjectSpending
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubjectSpendingForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class SubjectSpendingUpdateForm(SubjectSpendingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['acronym'].widget.attrs['id'] = "id_update_acronym"
        self.fields['budget'].widget.attrs['id'] = "id_update_budget"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_update_fiscal_terms"
        self.fields['accounting_book'].widget.attrs['id'] = "id_update_accounting_book"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class SubjectSpendingDeleteForm(SubjectSpendingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['acronym'].widget.attrs['id'] = "id_delete_acronym"
        self.fields['budget'].widget.attrs['id'] = "id_delete_budget"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_delete_fiscal_terms"
        self.fields['accounting_book'].widget.attrs['id'] = "id_delete_accounting_book"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"


# 節（支出）情報
class SectionSpendingForm(forms.ModelForm):
    class Meta:
        model = SectionSpending
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SectionSpendingForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class SectionSpendingUpdateForm(SectionSpendingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['print_format'].widget.attrs['id'] = "id_update_print_format"
        self.fields['acronym'].widget.attrs['id'] = "id_update_acronym"


class SectionSpendingDeleteForm(SectionSpendingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['print_format'].widget.attrs['id'] = "id_delete_print_format"
        self.fields['acronym'].widget.attrs['id'] = "id_delete_public_acronym"


# 科目（収入）情報
class SubjectIncomeForm(forms.ModelForm):
    class Meta:
        model = SubjectIncome
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubjectIncomeForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class SubjectIncomeUpdateForm(SubjectIncomeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['acronym'].widget.attrs['id'] = "id_update_acronym"
        self.fields['budget'].widget.attrs['id'] = "id_update_budget"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_update_fiscal_terms"
        self.fields['accounting_book'].widget.attrs['id'] = "id_update_accounting_book"
        self.fields['public_hall'].widget.attrs['id'] = "id_update_public_hall"


class SubjectIncomeDeleteForm(SubjectIncomeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['acronym'].widget.attrs['id'] = "id_delete_acronym"
        self.fields['budget'].widget.attrs['id'] = "id_delete_budget"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_delete_fiscal_terms"
        self.fields['accounting_book'].widget.attrs['id'] = "id_delete_accounting_book"
        self.fields['public_hall'].widget.attrs['id'] = "id_delete_public_hall"


# 節（収入）情報
class SectionIncomeForm(forms.ModelForm):
    class Meta:
        model = SectionIncome
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SectionIncomeForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-right"

class SectionIncomeUpdateForm(SectionIncomeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['id'] = "id_update_name"
        self.fields['print_format'].widget.attrs['id'] = "id_update_print_format"
        self.fields['acronym'].widget.attrs['id'] = "id_update_acronym"


class SectionIncomeDeleteForm(SectionIncomeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['readonly'] = "readonly"
        self.fields['name'].widget.attrs['id'] = "id_delete_name"
        self.fields['print_format'].widget.attrs['id'] = "id_delete_print_format"
        self.fields['acronym'].widget.attrs['id'] = "id_delete_public_acronym"

# 収入詳細
class IncomeRecordForm(forms.ModelForm):
    class Meta:
        model = IncomeRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IncomeRecordForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"
        self.fields['fixed_number'].widget.attrs['class'] = "h-6 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"

# 支出詳細
class SpendingRecordForm(forms.ModelForm):
    class Meta:
        model = SpendingRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpendingRecordForm, self).__init__(*args, **kwargs)
        for i ,n in enumerate( self.fields ):
            self.fields[ n ].widget.attrs['class'] = "bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"
        self.fields['fixed_number'].widget.attrs['class'] = "h-6 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"
        self.fields['rebersal_monies'].widget.attrs['class'] = "h-6 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"
        self.fields['behalf_pay'].widget.attrs['class'] = "h-6 bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 text-center"

# 一覧画面制御用
class PageManagerForm(forms.ModelForm):
    class Meta:
        model = PageManager
        fields = '__all__'

class PageManagerIncomeCreateForm(PageManagerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['id'] = "id_pagemanager_income_create_number"
        self.fields['income_select'].widget.attrs['id'] = "id_pagemanager_income_create_income_select"
        self.fields['accounting_book'].widget.attrs['id'] = "id_pagemanager_income_create_accounting_book"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_pagemanager_income_create_fiscal_terms"
        self.fields['spending_record'].widget.attrs['id'] = "id_pagemanager_income_create_spending_record"
        self.fields['income_record'].widget.attrs['id'] = "id_pagemanager_income_create_income_record"
        self.fields['public_hall'].widget.attrs['id'] = "id_pagemanager_income_create_public_hall"

class PageManagerSpendingCreateForm(PageManagerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['id'] = "id_pagemanager_spending_create_number"
        self.fields['income_select'].widget.attrs['id'] = "id_pagemanager_spending_create_income_select"
        self.fields['accounting_book'].widget.attrs['id'] = "id_pagemanager_spending_create_accounting_book"
        self.fields['fiscal_terms'].widget.attrs['id'] = "id_pagemanager_spending_create_fiscal_terms"
        self.fields['spending_record'].widget.attrs['id'] = "id_pagemanager_spending_create_spending_record"
        self.fields['income_record'].widget.attrs['id'] = "id_pagemanager_spending_create_income_record"
        self.fields['public_hall'].widget.attrs['id'] = "id_pagemanager_spending_create_public_hall"

IncomeCreateFormset = forms.inlineformset_factory(
    parent_model=IncomeRecord,
    model=PageManager,
    fields='__all__',
    form=PageManagerIncomeCreateForm,
    extra=1,can_delete=False,
)

SpendingCreateFormset = forms.inlineformset_factory(
    parent_model=SpendingRecord,
    model=PageManager,
    fields='__all__',
    form=PageManagerSpendingCreateForm,
    extra=1,can_delete=False
)
