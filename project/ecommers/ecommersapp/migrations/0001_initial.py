# Generated by Django 4.0.3 on 2022-04-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('mobno', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('password', models.CharField(default='', max_length=50)),
                ('c_password', models.CharField(default='', max_length=50)),
                ('profile_image', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'ecomp',
            },
        ),
    ]
