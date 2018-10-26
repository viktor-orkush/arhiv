from django.forms import ModelForm

from cedoinclusion.models import SedoAllowances, Departments, Personal


class SedoAllowanceForm(ModelForm):
    class Meta:
        model = SedoAllowances
        exclude = ('cyber_user',)


class DepartmentForm(ModelForm):
    class Meta:
        model = Departments


class PersonalForm (ModelForm):
    class Meta:
        model = Personal