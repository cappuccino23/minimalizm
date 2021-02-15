# Generated by Django 2.2 on 2020-06-25 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название модели')),
                ('image', models.ImageField(blank=True, upload_to='models_image')),
                ('short_desc', models.TextField(blank=True, verbose_name='Краткое описание модели')),
                ('description', models.TextField(blank=True, verbose_name='Описание модели')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена пошива модели')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory', verbose_name='Категория продукта')),
            ],
        ),
    ]
