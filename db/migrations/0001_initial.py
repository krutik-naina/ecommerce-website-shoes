# Generated by Django 3.2.23 on 2023-12-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('epassword', models.CharField(max_length=30)),
            ],
        ),
    ]
