from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request): #Funcao definida para lidar com requisicoes de registro de usuario
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)  # Cria um formulário com os dados enviados
        if user_form.is_valid():  # Verifica se o formulário é válido
            user_form.save()  # Salva o formulário
            return redirect('car_list')  # Redireciona para a página de car_list
    else:
        user_form = UserCreationForm()  # Instancia o UserCreationForm para o método GET

    return render(request, 'register.html', {'user_form': user_form})   
 