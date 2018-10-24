# Generated by Django 2.1.2 on 2018-10-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0003_auto_20181023_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='active',
            field=models.BooleanField(choices=[('1', 'פעיל'), ('2', 'לא פעיל')], max_length=1, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='measure_code',
            field=models.CharField(choices=[('1', 'ON TARGET'), ('2', 'LOW IS BETTER'), ('3', 'HIGH IS BETTER')], max_length=1, verbose_name='Measure_Code'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='measure_type',
            field=models.CharField(choices=[('1', 'ON TARGET'), ('2', 'LOW IS BETTER'), ('3', 'HIGH IS BETTER')], max_length=64, verbose_name='Measure_Type'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_type',
            field=models.CharField(choices=[('1', 'חצי שנתי'), ('2', 'שנתי')], max_length=1, verbose_name='Version_Types'),
        ),
    ]