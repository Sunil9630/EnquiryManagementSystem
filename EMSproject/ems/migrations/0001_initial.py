# Generated by Django 4.2.4 on 2023-08-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
