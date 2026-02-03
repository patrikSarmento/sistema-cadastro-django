# importa o modulo models do django que permite criar classes
# essas classes representam tabelas no banco de dados
from django.db import models


# define a classe Cliente que representa um cliente no sistema
# cada atributo da classe vira uma coluna na tabela do banco
class Cliente(models.Model):

    # campo que guarda o nome do cliente
    # charfield e usado para textos curtos
    # max_length define o tamanho maximo permitido no banco
    nome = models.CharField(max_length=100)

    # campo que guarda a data de nascimento do cliente
    # datefield e usado especificamente para datas
    # o django ja trata validacao e formato automaticamente
    data_nascimento = models.DateField()

    # campo que guarda o endereco do cliente
    # permite textos maiores como rua numero bairro e cidade
    endereco = models.CharField(max_length=255)

    # campo que guarda o telefone do cliente
    # e texto para permitir caracteres como parenteses espacos e hifen
    telefone = models.CharField(max_length=20)

    # campo que guarda a senha do cliente
    # esta como texto simples apenas para estudo
    # em sistemas reais o ideal e usar senha criptografada
    senha = models.CharField(max_length=50)

    # metodo especial que define como o objeto sera exibido
    # isso aparece por exemplo no admin do django
    # ao inves de mostrar Cliente object ele mostra o nome do cliente
    def __str__(self):
        return self.nome
