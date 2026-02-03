# importa funcoes prontas do django para renderizar paginas redirecionar urls
# e buscar objetos no banco retornando erro 404 se nao existir
from django.shortcuts import render, redirect, get_object_or_404

# importa o model Cliente que representa a tabela no banco de dados
from .models import Cliente

# importa o formulario baseado no model Cliente
from .forms import ClienteForm

# importa bibliotecas para gerar valores aleatorios
import random
import string


# funcao responsavel por gerar uma senha aleatoria para o cliente
def gerar_senha():
    # junta letras maiusculas minusculas e numeros
    caracteres = string.ascii_letters + string.digits
    # escolhe 8 caracteres aleatorios e junta tudo em uma string
    return ''.join(random.choice(caracteres) for _ in range(8))


# view que lista todos os clientes cadastrados
def lista_clientes(request):
    # busca todos os registros da tabela Cliente
    clientes = Cliente.objects.all()
    # envia a lista de clientes para o template de listagem
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


# view responsavel por criar um novo cliente
def criar_cliente(request):
    # verifica se o formulario foi enviado
    if request.method == 'POST':
        # cria o formulario com os dados enviados
        form = ClienteForm(request.POST)
        # valida os dados do formulario
        if form.is_valid():
            # cria o objeto sem salvar ainda no banco
            cliente = form.save(commit=False)
            # gera uma senha automatica para o cliente
            cliente.senha = gerar_senha()
            # salva o cliente no banco de dados
            cliente.save()
            # redireciona para a lista de clientes
            return redirect('lista_clientes')
    else:
        # cria um formulario vazio para exibicao inicial
        form = ClienteForm()

    # renderiza a pagina de criacao passando o formulario
    return render(request, 'clientes/criar_cliente.html', {'form': form})


# view responsavel por editar um cliente existente
def editar_cliente(request, id):
    # busca o cliente pelo id ou retorna erro se nao existir
    cliente = get_object_or_404(Cliente, id=id)

    # verifica se os dados foram enviados pelo formulario
    if request.method == 'POST':
        # cria o formulario preenchido com os dados atuais do cliente
        form = ClienteForm(request.POST, instance=cliente)
        # valida os dados enviados
        if form.is_valid():
            # salva as alteracoes no banco
            form.save()
            # redireciona para a lista de clientes
            return redirect('lista_clientes')
    else:
        # cria o formulario ja preenchido com os dados do cliente
        form = ClienteForm(instance=cliente)

    # renderiza a pagina de edicao passando o formulario
    return render(request, 'clientes/editar_cliente.html', {'form': form})


# view responsavel por excluir um cliente
def excluir_cliente(request, id):
    # busca o cliente pelo id ou retorna erro se nao existir
    cliente = get_object_or_404(Cliente, id=id)

    # confirma a exclusao quando o formulario e enviado
    if request.method == 'POST':
        # remove o cliente do banco de dados
        cliente.delete()
        # redireciona para a lista de clientes
        return redirect('lista_clientes')

    # renderiza a pagina de confirmacao de exclusao
    return render(request, 'clientes/excluir_cliente.html', {'cliente': cliente})
