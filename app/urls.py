from django.contrib import admin
from django.urls import path
from django.conf  import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view
from accounts.views import register_view, login_view, logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'), # Criando rota para acesso 'register_view)'
    path('login/',login_view, name =  'login'),  # Criando rota para acesso 'login_view'
    path('logout/',logout_view,  name =  'logout'),

    path('cars/', cars_view, name= 'cars_list'), # Criando rota para acesso 'car list'
    path('new_car/', new_car_view, name= 'new_car'),  # Criando rota para acesso 'new car'
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

