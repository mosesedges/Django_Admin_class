from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    context = {'name': 'Moses Ejele'}
    return render(request, 'homepage/index.html', context)
