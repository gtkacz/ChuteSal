# Generated by Django 4.1.4 on 2023-09-06 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('periodo_inscricao_comeco', models.DateField()),
                ('periodo_inscricao_fim', models.DateField()),
                ('periodo_jogos_comeco', models.DateField()),
                ('periodo_jogos_fim', models.DateField()),
                ('data_inicio_divulgacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('is_cup_manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('endereco', models.CharField(max_length=150)),
                ('cup_manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cup_manager', to='kicksal.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('posicao', models.IntegerField(default=0)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.campeonato')),
            ],
            options={
                'unique_together': {('posicao', 'campeonato'), ('nome', 'campeonato')},
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.unidade')),
            ],
            options={
                'unique_together': {('nome', 'unidade')},
            },
        ),
        migrations.AddField(
            model_name='funcionario',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.unidade'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='cup_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.funcionario'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='quadra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.quadra'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.unidade'),
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('rodada', models.IntegerField(default=0)),
                ('resultado_time1', models.IntegerField(default=0)),
                ('resultado_time2', models.IntegerField(default=0)),
                ('is_over', models.BooleanField(default=False)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.campeonato')),
                ('time1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='kicksal.time')),
                ('time2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='kicksal.time')),
            ],
            options={
                'unique_together': {('time1', 'time2', 'data', 'campeonato')},
            },
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(blank=True, max_length=50, null=True)),
                ('data_nascimento', models.DateField()),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kicksal.time')),
            ],
            options={
                'unique_together': {('nome', 'time')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='campeonato',
            unique_together={('nome', 'unidade')},
        ),
    ]
