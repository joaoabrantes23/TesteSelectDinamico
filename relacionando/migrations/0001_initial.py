# Generated by Django 4.2.3 on 2023-07-20 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade_caixa', models.CharField(choices=[], max_length=100)),
                ('ods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='relacionando.ods')),
            ],
        ),
    ]