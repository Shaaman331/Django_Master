from django.shortcuts import render
from cars.models import Car


# Create your views here.
def cars_view(request):
    print(request.GET)  # retorna o objeto GET request com informacao do usuario


    cars = Car.objects.filter(model__contains = 'Gol') #buscar modelos do objeto Car
    
    return render(
        request,
        'cars.html', # Renderiza  o template
        {'cars': cars}  # Passa o objeto cars para o template

        ) 
