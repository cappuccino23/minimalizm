# Generated by Django 2.2 on 2020-06-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='возраст'),
        ),
    ]
