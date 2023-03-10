# Generated by Django 4.1.4 on 2023-01-10 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter resort name (ex: Caesar blue)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(help_text='Unique id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter name of building (ex: Markus)', max_length=50, unique=True)),
                ('building_number', models.IntegerField(help_text='Building number')),
                ('resort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fagriskele.resort')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apartment_number', models.CharField(max_length=20)),
                ('floor', models.CharField(max_length=20)),
                ('bedrooms', models.CharField(max_length=20)),
                ('covered_gross', models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='Covered Gross Area')),
                ('balcony', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Balcony area sqm')),
                ('position', models.CharField(max_length=20)),
                ('price_in_gbp', models.IntegerField(null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fagriskele.building')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
