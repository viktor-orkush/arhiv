from django.contrib import admin
from .models import *


class ComputersAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Computers._meta.fields]

    class Meta:
        model = Computers

admin.site.register(Computers, ComputersAdmin)


class UsersAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.fields]

    class Meta:
        model = Users

admin.site.register(Users, UsersAdmin)


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


class CabinetsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Cabinets._meta.fields]

    class Meta:
        model = Cabinets

admin.site.register(Cabinets, CabinetsAdmin)


class ComputerTypesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ComputerTypes._meta.fields]

    class Meta:
        model = ComputerTypes

admin.site.register(ComputerTypes, ComputerTypesAdmin)