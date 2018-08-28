from django.shortcuts import render


def all_inclusion(request):
    name= "Test"
    current_day = "03.03.03"
    return render(request, 'cedoinclusion/all.html', locals())


def add_inclusion(request):
    return render(request, 'cedoinclusion/add.html', locals())