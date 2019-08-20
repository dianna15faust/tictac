from django.db import models

# Create your models here.

class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração, exemplo:quatidade)

    sigla   = models.CharField(max_length=2)
    nome    = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + " - " + self.nome

class Cidade(models.Model):
    nome        = models.CharField(max_length=50)
    estado      = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao   = models.TextField( blank=True, null=True, verbose_name="Descrição", help_text="Espaço para informações adicionais.")

    def __str__(self):
        return self.nome + " - " + self.estado.sigla

class Pessoa(models.Model):

    nome        = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    nascimento  = models.DateField(verbose_name='data de nascimento')
    email       = models.CharField(max_length=100)
    telefone    = models.CharField(max_length=20, help_text="(DD) XXXX-XXXX")
    endereco    = models.CharField(max_length=100)

    cidade      = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)

class Admin(models.Model):

    cpf                = models.CharField(max_length=11)
    carteira_trabalho  = models.CharField(max_length=100)

    pessoa             = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome + ' - ' + str(self.cpf)

class Leitor(models.Model):

    cartao_credito   = models.CharField(max_length=50)

    pessoa           = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome + ' - ' + str(self.cartao_credito)

class Acervo(models.Model):

    titulo        = models.CharField(max_length=50, help_text="Digite seu titulo da obra completo")
    genero       = models.CharField(max_length=100)
    descricao    = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)
class Pessoa(models.Model):

    nome        = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    genero       = models.CharField(max_length=100)
    descricao    = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + ' - ' + str(self.genero)
