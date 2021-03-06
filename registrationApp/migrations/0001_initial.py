# Generated by Django 3.2.9 on 2021-12-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email_address', models.EmailField(default=' ', max_length=300)),
                ('telephone', models.IntegerField()),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
                ('profile', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
