# Generated by Django 2.0.5 on 2018-08-28 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cedoinclusion', '0005_adressestest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdressesTest',
            new_name='Adresses',
        ),
        migrations.AlterModelOptions(
            name='adresses',
            options={'ordering': ('street',), 'verbose_name': 'Адреса', 'verbose_name_plural': 'Адреси'},
        ),
        migrations.RenameField(
            model_name='adresses',
            old_name='id_adres',
            new_name='id_adress',
        ),
    ]
