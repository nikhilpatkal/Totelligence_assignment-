# Generated by Django 4.2.7 on 2023-11-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0002_delete_user_regestration'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_regestration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(null=True)),
                ('user_email', models.TextField(null=True)),
                ('user_mobile', models.CharField(max_length=100)),
                ('user_address', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('reg_date', models.DateField(null=True)),
            ],
        ),
    ]
