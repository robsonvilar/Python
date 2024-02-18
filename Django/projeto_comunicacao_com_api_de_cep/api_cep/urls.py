from django.urls import path
from .views import teclado_telefone

urlpatterns = [
    path('teclado_telefone/', teclado_telefone, name='teclado_telefone'),
    # Outras URLs da sua aplicação...
]
