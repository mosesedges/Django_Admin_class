from django.shortcuts import render


def index(request):
    context = {'people': [{'name': 'John', 'age': '27', 'sex': 'Male', },
                          {'name': 'Rhoda', 'age': '47', 'sex': 'female', }]}

    return render(request, 'blog/index.html', context)
