# importa o modulo forms do django
# ele permite criar formularios de forma simples e integrada com os models
from django import forms

# importa o model Cliente para ligar o formulario a tabela do banco
from .models import Cliente


# define a classe ClienteForm que representa o formulario de cliente
# modelform cria automaticamente os campos com base no model
class ClienteForm(forms.ModelForm):

    # classe interna Meta usada para configurar o formulario
    class Meta:

        # informa qual model esse formulario representa
        # nesse caso o model Cliente
        model = Cliente

        # define quais campos do model vao aparecer no formulario
        # somente esses campos serao exibidos e editados pelo usuario
        # o campo senha fica de fora pois e gerado automaticamente
        fields = ['nome', 'data_nascimento', 'endereco', 'telefone']
