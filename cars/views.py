from django.shortcuts import render
from cars.models import Car


# Create your views here.
def cars_view(request):
    cars = Car.objects.all() #buscar modelos do objeto Car
    
    return render(
        request,
        'cars.html', # Renderiza  o template
        {'cars': cars}  # Passa o objeto cars para o template

        ) 
