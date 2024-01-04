# Generated by Django 3.2.23 on 2023-12-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_rename_contact_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.FileField(default=None, max_length=250, null=True, upload_to='upload/')),
                ('product', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]