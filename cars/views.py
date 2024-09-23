from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm


# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model') # Buscar todos os carros de forma ordernada no banco de dados
    search = request.GET.get('search')  # Retorna o objeto GET search com informacao do usuario

    if search:  # Pergunta se o usuario fez uma busca
        cars = Car.objects.filter(model__icontains = search) #Filtrar modelos do objeto Car search 
    
    return render(     # Retorna  a view renderizando o template
        request,
        'cars.html', # Renderiza  o template
        {'cars': cars}  # Passa o objeto cars para o template

        ) 

def new_car_view(request):  # Funcao para criar um new_car_view
    new_car_form = CarForm()  # Cria um objeto CarForm
    return render (request, 'new_car.html', {'new_car_form' :  new_car_form}) # Renderiza o template new_car.html e passa o objeto new_car_form