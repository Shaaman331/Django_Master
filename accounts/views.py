from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request): #Funcao definida para lidar com requisicoes de registro de usuario
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)  # Cria um formulário com os dados enviados
        if user_form.is_valid():  # Verifica se o formulário é válido
            user_form.save()  # Salva o formulário
            return redirect('login')  # Redireciona para a página de car_list
    else:
        user_form = UserCreationForm()  # Instancia o UserCreationForm para o método GET

    return render(request, 'register.html', {'user_form': user_form})   
 
def login_view(request): # Função para lidar com requisições de login de usuário
    if request.method == 'POST': #  Verifica se a requisição é POST, verifica se o usuario enviou um formulario com os dados de login
        username = request.POST['username']  # Se o método for "POST" pega o nome de usuario do formulario eviado
        password = request.POST['password']   # Se o método for "POST" pega a senha do formulario eviado
        user = authenticate(request, username=username, password=password) #Autentica o usuário usando as credenciais fornecidas, caso valída retornao o objeto User, caso contrário retorna None.

        if user is not None: #  Verifica se o usuário foi autenticado com sucesso
            login(request, user)  # Faz o login do usuário e armazena em ambas as secoes
            return redirect('cars_list') # Redireciona o usario para "cars_list"  caso o login seja bem sucedido

        else:  # Caso o login não seja bem sucedido

            login_form = AuthenticationForm()  # Instanciar o formulário corretamente
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})  # Renderiza a página de login com o formulário de login preenchido

def logout_view(request): # Função para lidar com requisições de logout de usuário
    logout(request)   # Chama a funcao  logout do django para fazer o logout do usuario 
    return redirect('cars_list') # Redireciona o usuário para a página de car_list

