from django.urls import path
from .views import (
    lista_clientes,
    criar_cliente,
    editar_cliente,
    excluir_cliente
)

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('novo/', criar_cliente, name='criar_cliente'),
    path('editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]
