# Generated by Django 4.2.7 on 2023-12-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuscode', models.TextField()),
                ('cusname', models.TextField()),
                ('cusemail', models.TextField()),
            ],
        ),
    ]
