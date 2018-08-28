# Generated by Django 2.0.5 on 2018-08-28 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cedoinclusion', '0003_auto_20180828_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cedoinclusion.Computers')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типи',
                'ordering': ('type',),
            },
        ),
        migrations.AlterModelOptions(
            name='cabinets',
            options={'ordering': ('cabinet_number',), 'verbose_name': 'Кабінет', 'verbose_name_plural': 'Кабінети'},
        ),
        migrations.AlterModelOptions(
            name='departments',
            options={'ordering': ('name',), 'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменти'},
        ),
        migrations.AlterModelOptions(
            name='ranks',
            options={'ordering': ('rank',), 'verbose_name': 'Ранг', 'verbose_name_plural': 'Ранги'},
        ),
        migrations.AlterModelOptions(
            name='sedoallowance',
            options={'ordering': ('our_income_number',), 'verbose_name': 'Включення', 'verbose_name_plural': 'Включення'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('name',), 'verbose_name': 'Прізвище', 'verbose_name_plural': 'Прізвища'},
        ),
    ]
