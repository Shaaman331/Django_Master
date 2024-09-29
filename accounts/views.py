from django.contrib.auth.forms import  UserCreationForm
from django.shortcuts import render


def register_view(request):  #Funcao definida para lidar com requisicoes de registro de usuario
    user_form =  UserCreationForm()   #Instancia a classe UserCreationForm para coletar informacoes do usuario
    return render (request, 'register.html', {'user_form': user_form}) #Renderiza a view com o formulario de registro


