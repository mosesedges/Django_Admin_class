from django.shortcuts import render
from .form import CustomerForm


def customers(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'Customers/index.html', context)
