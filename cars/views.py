from django.shortcuts import render
from cars.models import Car


# Create your views here.
def cars_view(request):
    search = request.GET.get('search')  # retorna o objeto GET search com informacao do usuario


    cars = Car.objects.filter(model__contains = search) #buscar modelos do objeto Car search 
    
    return render(
        request,
        'cars.html', # Renderiza  o template
        {'cars': cars}  # Passa o objeto cars para o template

        ) 
