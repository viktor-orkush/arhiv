import json

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from cedoinclusion.forms import SedoAllowanceForm, DepartmentsForm, PersonalForm, ComputerFormset
from cedoinclusion.models import *


class DeleteInclusion(DeleteView):
    model = SedoAllowances
    success_url = reverse_lazy('all_inclusion')


def sedoallowance_create(request):
    if request.method == "POST":
        allow_form = SedoAllowanceForm(request.POST)
        depart_form = DepartmentsForm(request.POST)
        cyber_user_form = PersonalForm(request.POST)
        if all([depart_form.is_valid(), allow_form.is_valid(), cyber_user_form.is_valid()]):
            department = depart_form.save()
            cyber_user= cyber_user_form.save()
            allowance = allow_form.save(commit=False)
            allowance.cyber_user = cyber_user
            allowance.department = department
            allowance.save()
            return redirect('all_inclusion')
    else:
        allow_form = SedoAllowanceForm()
        depart_form = DepartmentsForm()
        cyber_user_form = PersonalForm()
    return render(request, 'cedoinclusion/sedoallowances_create.html', {'allow_form': allow_form,
                                                                       'depart_form':depart_form,
                                                                       'person_form':cyber_user_form})


def computer_add(request):
    template_name = 'cedoinclusion/computer_add.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = ComputerFormset(request.GET or None)
    elif request.method == 'POST':
        formset = ComputerFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    pass
                    # Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('all_inclusion')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


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
        sedoAllowance = SedoAllowances.objects.get(id = sedoAllowance_id)
        computers = Computers.objects.filter(sedo_allowance = sedoAllowance_id)
        CAB_officeres = OfficersAdminsSedo.objects.all()
        return render(request, 'cedoinclusion/edit.html', locals())
    else:
        computers = Computers.objects.all()
        sedoAllowances = SedoAllowances.objects.all().order_by('our_income_date')
        return render(request, 'cedoinclusion/edit.html', locals())


def allowance_detail_info(request, sedoAllowance_id):
    computers = Computers.objects.filter(sedo_allowance = sedoAllowance_id)
    sedoAllowance = SedoAllowances.objects.get(id = sedoAllowance_id)
    return render(request, 'cedoinclusion/allowanceDetailInfo.html', locals())


def allUnit(request):
    sedoAllowances = SedoAllowances.objects.all()
    return render(request, 'cedoinclusion/allUnit.html', locals())


def add_inclusion(request):
    if request.method == 'GET':
        ranks = Ranks.objects.all()
        CAB_officeres = OfficersAdminsSedo.objects.all()
        return render(request, 'cedoinclusion/add.html', locals())
    else:
        data = request.POST
        department = data.get("department")

        military_number = data.get("military_number")
        city = data.get("city")
        street = data.get("street")
        building = data.get("building")

        cyber_rank = data.get("cyber_rank")
        cyber_name = data.get("cyber_name")
        cyber_phone = data.get("cyber_phone")

        worker_name = data.get("worker_name")
        worker_phone = data.get("worker_phone")

        our_income_number = data.get("our_income_number")
        our_income_date = data.get("our_income_date")

        alien_outcome_number = data.get("alien_outcome_number")
        alien_outcome_date = data.get("alien_outcome_date")

        serial_numbers = data.getlist("serial_number[]")
        computer_types = data.getlist("computer_type[]")
        ip = data.getlist("ip[]")
        room_numbers = data.getlist("room_number[]")

        CAB_officeres = data.get("CAB_officeres")

        department, dep_created = Departments.objects.get_or_create(name=department,
                                                                   military_number=military_number,
                                                                   city=city,
                                                                   street=street,
                                                                   building = building)
        try:
            rank = Ranks.objects.filter(id = cyber_rank).first()
        except Ranks.DoesNotExist:
            rank = None
        cyber_user, cyber_created = Personal.objects.get_or_create(rank = rank, name = cyber_name, phone = cyber_phone)
        try:
            CAB_officeres = OfficersAdminsSedo.objects.filter(id = CAB_officeres).first()
        except OfficersAdminsSedo.DoesNotExist:
            CAB_officeres = None
        sedo_allowance = SedoAllowances.objects.create(our_income_number = our_income_number,
                                                       our_income_date = our_income_date,
                                                       alien_outcome_number = alien_outcome_number,
                                                       alien_outcome_date = alien_outcome_date,
                                                       department = department,
                                                       CAB_officer=CAB_officeres,
                                                       cyber_user=cyber_user)

        for serial_num in serial_numbers:
            i = 0
            Computers.objects.create(sedo_allowance = sedo_allowance, serial_number = serial_num, type = computer_types[i], ip=ip[i], cabinet_number = room_numbers[i])
            i+=1
        return redirect('all_inclusion')


def ajax_add_depart(request):
    if request.POST.has_key('department'):
        department = request.POST['department']
        # department, dep_created = Departments.objects.get_or_create(name=department)
        return HttpResponse(json.dumps(department), mimetype='application/javascript')
    else:
        return render_to_response('ajaxexample.html', context_instance=RequestContext(request))