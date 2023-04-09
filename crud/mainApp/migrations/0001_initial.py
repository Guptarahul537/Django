# Generated by Django 4.1.1 on 2023-01-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("salary", models.IntegerField()),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=30)),
            ],
        ),
    ]
