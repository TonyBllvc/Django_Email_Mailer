# Generated by Django 5.0.4 on 2024-06-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtpToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=10)),
                ('otp', models.CharField(max_length=6)),
                ('tp_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]