# Generated by Django 4.2.5 on 2023-10-02 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0005_alter_jugador_dorsal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fichaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada', models.CharField(max_length=20)),
                ('equipofichaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipo.equipo')),
                ('jugadorfichaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipo.jugador')),
            ],
        ),
    ]
