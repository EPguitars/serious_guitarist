# Generated by Django 4.1.5 on 2023-01-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingblock',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trainingblock',
            name='if_ended',
            field=models.BooleanField(default=False),
        ),
    ]