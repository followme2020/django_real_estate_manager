# Generated by Django 4.1.4 on 2023-01-08 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fagriskele', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ['id']},
        ),
    ]
