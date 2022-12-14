# Generated by Django 4.1.2 on 2022-10-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagem',
            name='classe_Person',
            field=models.CharField(choices=[('Guerreiro', 'Guerreiro'), ('Mago', 'Mago'), ('Arqueiro', 'Arqueiro'), ('Necromante', 'Necromante')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='destino',
            field=models.CharField(choices=[('Glória', 'Glória eterna'), ('Vingança', 'Vingança sem fim'), ('Amor', 'Um belo amor')], default=0, max_length=10),
        ),
    ]
