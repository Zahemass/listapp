# Generated by Django 4.2.3 on 2023-07-22 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('do_list', '0007_particular_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particular_list',
            name='specific_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='do_list.name_list'),
        ),
    ]
