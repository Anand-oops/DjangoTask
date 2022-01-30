from django.shortcuts import render

from .models import Entry
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        if name and age:
            entry = Entry()
            entry.Name = name
            entry.Age = age
            entry.save()
    return render(request,'homepage.html')
