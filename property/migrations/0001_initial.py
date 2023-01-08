# Generated by Django 4.1.5 on 2023-01-07 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Places/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Property')),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Property_category', to='property.category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Property_place', to='property.place')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('feedback', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review_Property', to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Propertyimages/')),
                ('Property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Property_image', to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='proberty_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=django.utils.timezone.now)),
                ('date_to', models.DateField(default=django.utils.timezone.now)),
                ('guest', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('children', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_Property', to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
