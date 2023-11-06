# Generated by Django 4.2.7 on 2023-11-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('product_image', models.ImageField(upload_to='static/')),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('product_price', models.TextField()),
                ('product_link', models.TextField()),
            ],
        ),
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