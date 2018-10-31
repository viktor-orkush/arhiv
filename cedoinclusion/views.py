import json

from django.forms import formset_factory
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response
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

    all_department = Departments.objects.all()
    ranks = Ranks.objects.all()
    CAB_officeres = OfficersAdminsSedo.objects.all()

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
        # if formset.is_valid() and \
        #         depart_form.is_valid() and \
        #         allow_form.is_valid() and \
        #         cyber_user_form.is_valid():
            try:
                CAB_officere = OfficersAdminsSedo.objects.filter(id=CAB_officere).first()
            except OfficersAdminsSedo.DoesNotExist:
                CAB_officere = None
            # department, created = Departments.objects.get_or_create(**depart_form.cleaned_data)
            try:
                name_cl = depart_form.cleaned_data
                name = name_cl.get('name')
                department = Departments.objects.filter(name = name).first()
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
                print(form)
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
    return render(request, 'cedoinclusion/sedoallowances_create.html', {'allow_form': allow_form,
                                                                        'depart_form': depart_form,
                                                                        'person_form': cyber_user_form,
                                                                        'formset': formset,
                                                                        'ranks':ranks,
                                                                        'all_department':all_department,
                                                                        'CAB_officeres':CAB_officeres})


def all_inclusion(request):
    computers = Computers.objects.all()
    sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')
    return render(request, 'cedoinclusion/all.html', locals())


def delete_inclusion(request, pk):
    sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')
    return render(request, 'cedoinclusion/all.html', locals())


def edit_department(request, sedoAllowance_id):
    if request.method == 'GET':
        ranks = Ranks.objects.all()
        sedoAllowance = SedoAllowances.objects.get(id=sedoAllowance_id)
        computers = Computers.objects.filter(sedo_allowance=sedoAllowance_id)
        CAB_officeres = OfficersAdminsSedo.objects.all()
        return render(request, 'cedoinclusion/edit.html', locals())
    else:
        computers = Computers.objects.all()
        sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')
        return render(request, 'cedoinclusion/edit.html', locals())


def allowance_detail_info(request, sedoAllowance_id):
    computers = Computers.objects.filter(sedo_allowance=sedoAllowance_id)
    sedoAllowance = SedoAllowances.objects.get(id=sedoAllowance_id)
    return render(request, 'cedoinclusion/allowanceDetailInfo.html', locals())


def allUnit(request):
    sedoAllowances = SedoAllowances.objects.all()
    return render(request, 'cedoinclusion/allUnit.html', locals())