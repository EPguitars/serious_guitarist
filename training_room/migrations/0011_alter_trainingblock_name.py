# Generated by Django 4.1.5 on 2023-01-31 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("training_room", "0010_alter_trainingblock_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainingblock",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
