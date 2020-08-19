from django.http import HttpResponse
from django.shortcuts import render

from model.models import WorkhouseAge


def showall(request):
    obj = WorkhouseAge.objects.first()
    obj_list = WorkhouseAge.objects.all()
    return render(request, 'showall.html', context=locals())
