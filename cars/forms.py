from django import forms
from cars.models import Brand, Car

#Criando Form usuário de Cadastro de marca

class CarForm(forms.Form): 
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):  #Método para salvar os dados do formulário

        car = Car(   #Criando um objeto Car
            model = self.cleaned_data['model'], # Pegando os dados do formulário
            brand = self.cleaned_data['brand'],  
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save() # Salva o objeto no banco de dados
        return car
    
class CarModelForm(forms.ModelForm):  #Criando um formulário de modelo de carro usando ModelForm
    class Meta:
        model = Car
        fields = "__all__"



