# Generated by Django 4.1.4 on 2023-10-31 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksal', '0009_alter_jogador_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
