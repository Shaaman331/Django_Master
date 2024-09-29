from django import forms
from cars.models import Car

#Criando Form usuário de Cadastro de marca
    
class CarModelForm(forms.ModelForm):  #Criando um formulário de modelo de carro usando ModelForm
    class Meta:   #Definindo a classe Meta para especificar o modelo de dados

        model = Car   #Definindo o modelo de dados
        fields = "__all__"   #Definindo os campos do formulário


    def clean_value(self):
        value = self.cleaned_data.get('value') 
        if value < 20000: 
            self.add_error('value','Valor minimo do carro deve ser maior que 20000') 
        return value 

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year','Ano de fabricação deve ser maior que 2000')
        return factory_year
    








