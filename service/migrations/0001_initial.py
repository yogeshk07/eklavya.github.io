# Generated by Django 4.1.4 on 2023-04-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_number', models.CharField(max_length=50)),
                ('service_text', models.TextField()),
            ],
        ),
    ]
