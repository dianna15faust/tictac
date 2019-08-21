# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),

    #URLS de cadastros
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('cadastrar/admin/', AdminCreate.as_view(), name="cadastrar-admin"),
    path('cadastrar/leitor/', LeitorCreate.as_view(), name="cadastrar-leitor"),
    path('cadastrar/acervo/', AcervoCreate.as_view(), name="cadastrar-acervo"),
    path('cadastrar/locacao/', LocacaoCreate.as_view(), name="cadastrar-locacao"),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
    path('editar/admin/<int:pk>/', AdminUpdate.as_view(), name="editar-admin"),
    path('editar/leitor/<int:pk>/', LeitorUpdate.as_view(), name="editar-leitor"),
    path('editar/acervo/<int:pk>/', AcervoUpdate.as_view(), name="editar-acervo"),
    path('editar/locacao/<int:pk>/', LocacaoUpdate.as_view(), name="editar-locacao"),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="deletar-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="deletar-cidade"),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="deletar-pessoa"),
    path('excluir/admin/<int:pk>/', AdminDelete.as_view(), name="deletar-admin"),
    path('excluir/leitor/<int:pk>/', LeitorDelete.as_view(), name="deletar-leitor"),
    path('excluir/acervo/<int:pk>/', AcervoDelete.as_view(), name="deletar-acervo"),
    path('excluir/locacao/<int:pk>/', LocacaoDelete.as_view(), name="deletar-locacao"),

    path('lista/estado/', EstadoList.as_view(), name="lista_estado"),
    path('lista/cidade/', CidadeList.as_view(), name="lista_cidade"),
    path('lista/pessoa/', PessoaList.as_view(), name="lista_pessoa"),
    path('lista/admin/', AdminList.as_view(), name="lista_admin"),
    path('lista/leitor/', LeitorList.as_view(), name="lista_leitor"),
    path('lista/acervo/', AcervoList.as_view(), name="lista_acervo"),
    path('lista/locacao/', LocacaoList.as_view(), name="lista_locacao"),


]
