from django.shortcuts import render, redirect

from cedoinclusion.models import *


def all_inclusion(request):
    computers = Computers.objects.all()
    sedoAllowances = SedoAllowance.objects.all().order_by('our_income_date')
    return render(request, 'cedoinclusion/all.html', locals())


def delete_department(request):
    computers = Computers.objects.all()
    sedoAllowances = SedoAllowance.objects.all().order_by('our_income_date')
    return render(request, 'cedoinclusion/all.html', locals())


def edit_department(request, sedoAllowance_id):
    if request.method == 'GET':
        ranks = Ranks.objects.all()
        sedoAllowance = SedoAllowance.objects.get(id = sedoAllowance_id)
        computers = Computers.objects.filter(sedo_allowance = sedoAllowance_id)
        CAB_officeres = OfficersAdminsSedo.objects.all()
        return render(request, 'cedoinclusion/edit.html', locals())
    else:
        computers = Computers.objects.all()
        sedoAllowances = SedoAllowance.objects.all().order_by('our_income_date')
        return render(request, 'cedoinclusion/edit.html', locals())


def allowance_detail_info(request, sedoAllowance_id):
    computers = Computers.objects.filter(sedo_allowance = sedoAllowance_id)
    sedoAllowance = SedoAllowance.objects.get(id = sedoAllowance_id)
    return render(request, 'cedoinclusion/allowanceDetailInfo.html', locals())


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
        room_numbers = data.getlist("room_number[]")

        CAB_officeres = data.get("CAB_officeres")

        adresses, adr_created = Adresses.objects.get_or_create(military_number=military_number, city=city,
                                                               street=street, building = building)
        department, dep_created = Departments.objects.get_or_create(adress=adresses, name=department)
        try:
            rank = Ranks.objects.filter(id = cyber_rank).first()
        except Ranks.DoesNotExist:
            rank = None
        cyber_user, cyber_created = Personal.objects.get_or_create(rank = rank, name = cyber_name, phone = cyber_phone)
        worker_user, worker_created = Personal.objects.get_or_create(name = worker_name, phone = worker_phone)
        try:
            CAB_officeres = OfficersAdminsSedo.objects.filter(id = CAB_officeres).first()
        except OfficersAdminsSedo.DoesNotExist:
            CAB_officeres = None
        sedo_allowance, sedo_allow_created = SedoAllowance.objects.get_or_create(our_income_number = our_income_number,
                                                                                 our_income_date = our_income_date,
                                                                                 alien_outcome_number = alien_outcome_number,
                                                                                 alien_outcome_date = alien_outcome_date,
                                                                                 department = department,
                                                                                 CAB_officer=CAB_officeres,
                                                                                 cyber_user=cyber_user,
                                                                                 worker_user=worker_user)

        for serial_num in serial_numbers:
            i = 0
            Computers.objects.create(sedo_allowance = sedo_allowance, serial_number = serial_num, type = computer_types[i], cabinet_number = room_numbers[i])
            i+=1
        return redirect('all_inclusion')