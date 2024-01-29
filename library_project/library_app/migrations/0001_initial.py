# Generated by Django 5.0.1 on 2024-01-29 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_on', models.DateField()),
                ('copies_available', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=50)),
                ('pages', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.bookcategory')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.library')),
            ],
        ),
    ]