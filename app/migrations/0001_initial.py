# Generated by Django 5.0.6 on 2024-06-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Dhaka', 'Dhaka'), ('Gazipur', 'Gazipur'), ('Narayanganj', 'Narayanganj'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka'), ('Dhaka', 'Dhaka')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimage')),
                ('filefield', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
