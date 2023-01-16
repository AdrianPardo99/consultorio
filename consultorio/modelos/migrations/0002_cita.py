# Generated by Django 4.1.5 on 2023-01-16 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('fecha', models.DateTimeField(verbose_name='Fecha y horario de cita')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='citas', to='modelos.paciente', verbose_name='paciente')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': 'cita',
            },
        ),
    ]