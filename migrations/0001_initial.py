# Generated by Django 4.2.6 on 2023-11-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=50)),
                ('mb', models.IntegerField()),
                ('em', models.EmailField(max_length=254)),
                ('ps', models.CharField(max_length=16)),
            ],
        ),
    ]
