# Generated by Django 3.2.5 on 2021-07-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Action', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=100)),
                ('a_age', models.IntegerField()),
                ('a_no_movies', models.IntegerField()),
            ],
        ),
    ]
