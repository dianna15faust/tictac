from django.db import models

# Create your models here.

class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração, exemplo:quatidade)

    sigla   = models.CharField(max_length=2)
    nome    = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + " - " + self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao = models.TextField(
        blank=True, null=True, verbose_name="Descrição",
        help_text="Espaço para colocar qualquer informação."
    )

    def __str__(self):
        return self.nome + '/' + self.estado.sigla

class Pessoa(models.Model):

    nome        = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    nascimento  = models.DateField(verbose_name='data de nascimento')
    email       = models.CharField(max_length=100)
    endereco    = models.CharField(max_length=100)

    cidade      = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.nome, self.nascimento, self.email)

class Admin(models.Model):

    cpf                = models.CharField(max_length=11)
    carteira_trabalho  = models.CharField(max_length=100)

    pessoa             = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.cpf + ' - ' + str(self.pessoa.nome)

class Leitor(models.Model):

    cartao = models.CharField(max_length=50)

    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.cartao + ' - ' + str(self.pessoa.nome)

class Acervo(models.Model):

    titulo        = models.CharField(max_length=50, help_text="Digite seu titulo da obra completo")
    genero       = models.CharField(max_length=100)
    descricao    = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}/{}".format(self.titulo, self.genero, self.descricao)

class Locacao(models.Model):

    valor         = models.CharField(max_length=50)
    data_entrega  = models.DateField(verbose_name='data da locação')
    data_devolucao    = models.DateField(verbose_name='data de devolução')
    multa         = models.CharField(max_length=50)

    acervo        = models.ForeignKey(Acervo, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor + ' - ' + str(self.acervo.titulo)
