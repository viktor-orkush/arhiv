from django.forms import ModelForm, formset_factory
from django import forms
from cedoinclusion.models import SedoAllowances, Departments, Personal


class SedoAllowanceForm(ModelForm):
    class Meta:
        model = SedoAllowances
        exclude = ('cyber_user', 'department', 'data')
        fields = '__all__'
        widgets = {
            'our_income_number': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'вхідний номер'}),
            'our_income_date': forms.TextInput(attrs={'class': 'form-control',
                                                      'type': "date",
                                                      'id': "example-date-input"
                                                      }),
            'alien_outcome_number': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'вихідний підрозділу'}),
            'alien_outcome_date': forms.TextInput(attrs={'class': 'form-control',
                                                        'type': "date",
                                                         'id':"example-date-input"
                                                        }),
            'CAB_officer': forms.Select(attrs={'class': 'form-control'}),
        }

class DepartmentsForm(ModelForm):

    class Meta:
        model = Departments
        fields = '__all__'
        # labels = {'name': 'Підрозділ', 'military_number': '№ в/м'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Підрозділ',
                                           'list': 'cars',
                                           'required': 'required'}),
            'military_number': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': '№ В/М'}),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Місто'}),
            'street': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Вулиця'}),
            'building': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '№ будинку'}),
        }


class PersonalForm (ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

        widgets = {
            'rank': forms.Select(attrs={'class': 'form-control',
                                           'placeholder': 'Звання'}),
            'personal_name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Прізвище'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Телефон'}),
        }


class ComputerForm(forms.Form):
    serial_number = forms.CharField(
        label='Серійний номер',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Серійний номер',
            'required': "required"
        })
    )
    type = forms.CharField(
        # required=False,
        # error_messages={'required': 'Please enter your name'},
        label='Тип АРМ',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тип АРМ'
        })
    )
    ip = forms.GenericIPAddressField(
        label='ІР адреса',
        # error_messages={'required': 'Please enter your name'},
        # help_text= 'ІР адресу вводити в форматі 0.0.0.0',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ІР адреса',
            'pattern' : "^([0-9]{1,3}\.){3}[0-9]{1,3}$"
        })
    )
    cabinet_number = forms.CharField(
        label='Номер каб.',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер каб.'
        })
    )

ComputerFormset = formset_factory(ComputerForm)