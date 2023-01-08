# Generated by Django 4.1.5 on 2023-01-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=60)),
                ('logo', models.ImageField(upload_to='settings/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('fb_link', models.URLField(max_length=500)),
                ('instagram_link', models.URLField(max_length=500)),
                ('twitter_link', models.URLField(max_length=500)),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
    ]