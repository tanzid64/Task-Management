# Generated by Django 4.2.7 on 2023-12-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_remove_category_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='catagories',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]