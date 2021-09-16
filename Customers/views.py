from django.shortcuts import render


def customers(request):
    return render(request, 'Customers/index.html')
