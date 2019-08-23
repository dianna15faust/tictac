from django.shortcuts import render

#Importa todas as classes do models.py
from .models import *

#Importação que chamas as URL's pelo "name" delas
from django.urls import reverse_lazy

#Importar as classes Views para inserir. alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#IMporta o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

from django.views.generic.list import ListView

#Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "adocao/index.html"


# Página "Sobre"
class SobreView(TemplateView):
    template_name = "adocao/sobre.html"

# Página "Contato"
class ContatoView(TemplateView):
    template_name = "adocao/contato.html"

# Página "Curriculo"
class CurriculoView(TemplateView):
    template_name = "adocao/curriculo.html"

####################################### INSERIR #########################################################################

class EstadoCreate(LoginRequiredMixin, CreateView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Estado
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de inserir um registro. Informe o nome
    success_url = reverse_lazy("index")
    #Quais campos devem aparecer no formulario?
    fields = ['sigla', 'nome']

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"
        return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['nome', 'estado', 'descricao']

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"
        return context


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['nome', 'nascimento' , 'email', 'endereco', 'cidade']

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novas Pessoas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"

        return context

class AdminCreate(LoginRequiredMixin, CreateView):
    model = Admin
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['cpf', 'carteira_trabalho', 'pessoa' ]

    def get_context_data(self, *args, **kwargs):
        context = super(AdminCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Admin"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"

        return context

class LeitorCreate(LoginRequiredMixin, CreateView):
    model = Leitor
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['cartao', 'pessoa' ]

    def get_context_data(self, *args, **kwargs):
        context = super(LeitorCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Leitor"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"

        return context

class AcervoCreate(LoginRequiredMixin, CreateView):
    model = Acervo
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['titulo','genero','descricao' ]

    def get_context_data(self, *args, **kwargs):
        context = super(AcervoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Acervo"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"

        return context
class LocacaoCreate(LoginRequiredMixin, CreateView):
    model = Locacao
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['valor','data_entrega','data_devolucao','multa' ]

    def get_context_data(self, *args, **kwargs):
        context = super(LocacaoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Locar"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-danger"

        return context
####################################### ALTERAR #########################################################################

class EstadoUpdate(UpdateView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Estado
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de inserir um registro. Informe o nome
    success_url = reverse_lazy("index")
    #Quais campos devem aparecer no formulario?
    fields = ['sigla', 'nome']

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Estados"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

class CidadeUpdate(UpdateView):
    model = Cidade
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['nome', 'estado', 'descricao']

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Cidades"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

class PessoaUpdate(UpdateView):
    model = Pessoa
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['nome', 'nascimento' , 'email', 'endereco', 'cidade']

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Pessoa"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

class AdminUpdate(UpdateView):
    model = Admin
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['cpf', 'carteira_trabalho', 'pessoa']

    def get_context_data(self, *args, **kwargs):
        context = super(AdminUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Admin"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

class LeitorUpdate(UpdateView):
    model = Leitor
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['cartao_credito', 'pessoa' ]

    def get_context_data(self, *args, **kwargs):
        context = super(LeitorUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Leitor"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

class AcervoUpdate(UpdateView):
    model = Acervo
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['titulo','genero','descricao' ]

    def get_context_data(self, *args, **kwargs):
        context = super(AcervoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Acervo"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context
class LocacaoUpdate(UpdateView):
    model = Locacao
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')
    fields = ['valor','data_entrega','data_devolucao','multa' ]

    def get_context_data(self, *args, **kwargs):
        context = super(LocacaoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Locação"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-danger"

        return context

####################################### DELETAR #########################################################################

class EstadoDelete(DeleteView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Estado
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de excluir um registro. Informe o nome
    success_url = reverse_lazy("index")


    def get_context_data(self, *args, **kwargs):
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'adocao/formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir essa Pessoa ? "
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context
class   AdminDelete(DeleteView):
    model = Admin
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("index")


    def get_context_data(self, *args, **kwargs):
        context = super(AdminDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context
class LeitorDelete(DeleteView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Leitor
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de excluir um registro. Informe o nome
    success_url = reverse_lazy("index")


    def get_context_data(self, *args, **kwargs):
        context = super(LeitorDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class AcervoDelete(DeleteView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Acervo
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de excluir um registro. Informe o nome
    success_url = reverse_lazy("index")


    def get_context_data(self, *args, **kwargs):
        context = super(AcervoDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context
class LocacaoDelete(DeleteView):
    #Define qual o modelo pra essa classe que vai criar o form
    model = Locacao
    #Qual o html que será utilizado
    template_name = "adocao/formulario.html"
    #Para onde redirecionar o usuário depois de excluir um registro. Informe o nome
    success_url = reverse_lazy("index")


    def get_context_data(self, *args, **kwargs):
        context = super(LocacaoDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

####################################### LISTAR #########################################################################

class EstadoList(ListView):
    model = Estado
    template_name = "adocao/lista_estado.html"
class CidadeList(ListView):
    model = Cidade
    template_name = "adocao/lista_cidade.html"
class PessoaList(ListView):
    model = Pessoa
    template_name = "adocao/lista_pessoa.html"
class AdminList(ListView):
    model = Admin
    template_name = "adocao/lista_admin.html"
class LeitorList(ListView):
    model = Leitor
    template_name = "adocao/lista_leitor.html"
class AcervoList(ListView):
    model = Acervo
    template_name = "adocao/lista_acervo.html"
class LocacaoList(ListView):
    model = Locacao
    template_name = "adocao/lista_locacao.html"
