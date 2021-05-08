# Generated by Django 3.2 on 2021-04-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartella',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cartella', models.CharField(help_text='Inserire il nome della cartella', max_length=128)),
                ('tempo_riproduzione', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Cartella',
                'verbose_name_plural': 'Cartelle',
            },
        ),
    ]