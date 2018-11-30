import json

from django.core.paginator import Paginator
from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from cedoinclusion.forms import SedoAllowanceForm, DepartmentsForm, PersonalForm, ComputerFormset, ComputerForm
from cedoinclusion.models import *


class DeleteInclusion(DeleteView):
    model = SedoAllowances
    success_url = reverse_lazy('all_inclusion')


def sedoallowance_create(request):
    ComputerFormSet = formset_factory(ComputerForm)
    allow_form = SedoAllowanceForm()
    depart_form = DepartmentsForm()
    cyber_user_form = PersonalForm()
    formset = ComputerFormset()
    if request.method == "POST":
        formset = ComputerFormSet(request.POST, request.FILES)
        allow_form = SedoAllowanceForm(request.POST)
        depart_form = DepartmentsForm(request.POST)
        cyber_user_form = PersonalForm(request.POST)
        CAB_officere = request.POST.get("CAB_officer")

        a = formset.is_valid()
        b = depart_form.is_valid()
        c = allow_form.is_valid()
        d = cyber_user_form.is_valid()
        if a and b and c and d:
            try:
                CAB_officere = OfficersAdminsSedo.objects.filter(id=CAB_officere).first()
            except OfficersAdminsSedo.DoesNotExist:
                CAB_officere = None
            # department, created = Departments.objects.get_or_create(**depart_form.cleaned_data)
            try:
                name_cl = depart_form.cleaned_data
                name = name_cl.get('name')
                department = Departments.objects.get(name = name)
            except Departments.DoesNotExist:
                department = depart_form.save()
            cyber_user = cyber_user_form.save()
            allowance = allow_form.save(commit=False)
            allowance.cyber_user = cyber_user
            allowance.department = department
            allowance.CAB_officer = CAB_officere
            allowance.save()
            # ****************Add computer ARM********************
            for form in formset:
                # print(form)
                form_clean = form.cleaned_data
                serial_number = form_clean.get('serial_number')
                ip = form_clean.get('ip')
                type = form_clean.get('type')
                cabinet_number = form_clean.get('cabinet_number')
                if serial_number:
                    Computers(sedo_allowance=allowance ,serial_number=serial_number, ip=ip, type=type, cabinet_number=cabinet_number).save()
            return redirect('all_inclusion')
        else:
            errors = formset.errors

    all_department = Departments.objects.all()
    # ranks = Ranks.objects.all()
    # CAB_officeres = OfficersAdminsSedo.objects.all()
    return render(request, 'cedoinclusion/sedoallowances_create.html', {'allow_form': allow_form,
                                                                        'depart_form': depart_form,
                                                                        'person_form': cyber_user_form,
                                                                        'formset': formset,
                                                                        'all_department':all_department})


def sedo_allowance_edit(request, pk):
    sedo_allowance = get_object_or_404(SedoAllowances, pk=pk)
    ComputerInLineFormSet = inlineformset_factory(SedoAllowances,
                                                  Computers,
                                                  fields=('id','serial_number',
                                                                                     'type',
                                                                                     'ip',
                                                                                     'cabinet_number',),
                                                  extra=0,
                                                  can_delete=True,
                                                  )
    sedo_allowance_form = SedoAllowanceForm(request.POST or None, instance=sedo_allowance)
    computers_formset = ComputerInLineFormSet(request.POST or None, request.FILES or None, instance=sedo_allowance)
    department_form = DepartmentsForm(request.POST or None, instance=sedo_allowance.department)
    cyber_user_form = PersonalForm(request.POST or None, instance=sedo_allowance.cyber_user)
    if request.method == 'POST':
        a = computers_formset.is_valid()
        b = sedo_allowance_form.is_valid()
        c = department_form.is_valid()
        d = cyber_user_form.is_valid()
        if sedo_allowance_form.is_valid() and department_form.is_valid() and cyber_user_form.is_valid():
            sedo_allowance = sedo_allowance_form.save(commit=False)
            department = department_form.save()
            cyber_user = cyber_user_form.save()
            sedo_allowance.save()
            if computers_formset.is_valid():
                computers_formset.save()
                return redirect('all_inclusion')

        errors = computers_formset.errors
    return render(request, 'cedoinclusion/sedoallowances_edit.html', {'allow_form': sedo_allowance_form,
                                                                      'depart_form': department_form,
                                                                      'person_form': cyber_user_form,
                                                                      'formset': computers_formset})


def all_inclusion(request):
    computers = Computers.objects.all()
    sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')

    paginator = Paginator(sedoAllowances, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'cedoinclusion/all.html', {'sedoAllowances':contacts, 'computers':computers})


def delete_inclusion(request, pk):
    sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')
    return render(request, 'cedoinclusion/all.html', locals())


def allowance_detail_info(request, sedoAllowance_id):
    computers = Computers.objects.filter(sedo_allowance=sedoAllowance_id)
    sedoAllowance = SedoAllowances.objects.get(id=sedoAllowance_id)
    return render(request, 'cedoinclusion/allowanceDetailInfo.html', locals())


def allUnit(request):
    sedoAllowances = SedoAllowances.objects.all()
    return render(request, 'cedoinclusion/allUnit.html', locals())
