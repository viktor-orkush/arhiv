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
    name = forms.CharField(
        label='Computer Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
ComputerFormset = formset_factory(ComputerForm, extra=1)