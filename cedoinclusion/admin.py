from django.contrib import admin
from .models import *


class ComputersAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Computers._meta.fields]
    # inlines = [PersonalInline]

    class Meta:
        model = Computers

admin.site.register(Computers, ComputersAdmin)


class PersonalAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Personal._meta.fields]

    class Meta:
        model = Personal

admin.site.register(Personal, PersonalAdmin)


class RanksAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Ranks._meta.fields]

    class Meta:
        model = Ranks

admin.site.register(Ranks, RanksAdmin)


class DepartmentsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Departments._meta.fields]

    class Meta:
        model = Departments

admin.site.register(Departments, DepartmentsAdmin)


class SedoAllowancesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SedoAllowances._meta.fields]

    class Meta:
        model = SedoAllowances

admin.site.register(SedoAllowances, SedoAllowancesAdmin)


class OfficersAdminsSedoAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OfficersAdminsSedo._meta.fields]

    class Meta:
        model = OfficersAdminsSedo

admin.site.register(OfficersAdminsSedo, OfficersAdminsSedoAdmin)