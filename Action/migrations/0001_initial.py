# Generated by Django 3.2.5 on 2021-07-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_age', models.IntegerField()),
                ('s_roll', models.CharField(max_length=10)),
                ('s_email', models.EmailField(max_length=100)),
            ],
        ),
    ]