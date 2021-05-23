# Generated by Django 3.2 on 2021-05-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.BigIntegerField(max_length=20)),
            ],
        ),
    ]
