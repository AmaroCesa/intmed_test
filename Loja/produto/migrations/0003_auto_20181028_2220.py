# Generated by Django 2.1.2 on 2018-10-29 01:20

from django.db import migrations, models
import produto.models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20181028_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_desc',
            field=models.CharField(choices=[('Processadores', 'Processadores'), ('Memória RAM', 'Memória RAM'), ('Disco Rígido/SSD', 'Disco Rígido/SSD'), ('Placa de Vídeo', 'Placa de Vídeo'), ('Gabinete', 'Gabinete'), ('Placa mãe', 'Placa mãe'), ('Fonte', 'Fonte')], max_length=32, validators=[produto.models.categoria_range]),
        ),
    ]
