# Generated by Django 2.2.4 on 2019-08-23 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acervo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Digite seu titulo da obra completo', max_length=50)),
                ('genero', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tefelone',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cidade',
            name='descricao',
            field=models.TextField(blank=True, help_text='Espaço para colocar qualquer informação.', null=True, verbose_name='Descrição'),
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=50)),
                ('data_entrega', models.DateField(verbose_name='data da locação')),
                ('data_devolucao', models.DateField(verbose_name='data de devolução')),
                ('multa', models.CharField(max_length=50)),
                ('acervo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Acervo')),
            ],
        ),
    ]