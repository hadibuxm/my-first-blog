# Generated by Django 3.0.6 on 2020-05-27 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_form',
            name='mobile_no',
            field=models.CharField(max_length=11),
        ),
    ]
