from django.forms import ModelForm, formset_factory
from django import forms
from cedoinclusion.models import SedoAllowances, Departments, Personal


class SedoAllowanceForm(ModelForm):
    class Meta:
        model = SedoAllowances
        exclude = ('cyber_user', 'department')


class DepartmentsForm(ModelForm):

    class Meta:
        model = Departments
        fields = '__all__'
        labels = {'name': 'Підрозділ', 'military_number': '№ в/м'}


class PersonalForm (ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'


class ComputerForm(forms.Form):
    serial_number = forms.CharField(
        label='Серійний номер',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Серійний номер'
        })
    )
    type = forms.CharField(
        label='Тип АРМ',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тип АРМ'
        })
    )
    ip = forms.GenericIPAddressField(
        label='ІР адреса',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ІР адреса'
        })
    )
    cabinet_number = forms.CharField(
        label='Номер каб.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер каб.'
        })
    )

    # def __init__(self, *args, **kwargs):
    #     super(ComputerForm, self).__init__(*args, **kwargs)

    # # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(ComputerForm, self).__init__(*args, **kwargs)

ComputerFormset = formset_factory(ComputerForm)

# FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
#                                             form=FamilyMemberForm, extra=1)