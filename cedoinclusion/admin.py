from django.contrib import admin
from .models import *


# class PersonalInline(admin.TabularInline):
#     model = Personal
#     extra = 0


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


class AdressesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Adresses._meta.fields]

    class Meta:
        model = Adresses

admin.site.register(Adresses, AdressesAdmin)


class DepartmentsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Departments._meta.fields]

    class Meta:
        model = Departments

admin.site.register(Departments, DepartmentsAdmin)


class SedoAllowanceAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SedoAllowance._meta.fields]

    class Meta:
        model = SedoAllowance

admin.site.register(SedoAllowance, SedoAllowanceAdmin)


class OfficersAdminsSedoAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OfficersAdminsSedo._meta.fields]

    class Meta:
        model = OfficersAdminsSedo

admin.site.register(OfficersAdminsSedo, OfficersAdminsSedoAdmin)

# class ComputerTypesAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ComputerTypes._meta.fields]
#
#     class Meta:
#         model = ComputerTypes
#
# admin.site.register(ComputerTypes, ComputerTypesAdmin)