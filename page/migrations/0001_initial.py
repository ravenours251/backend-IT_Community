# Generated by Django 3.1.7 on 2021-03-08 07:18

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('author', models.CharField(max_length=56, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='blog/cover/')),
                ('thumbnail', models.ImageField(blank=True, default='blog/thumbnail/default.png', upload_to='blog/thumbnail')),
                ('slug', models.SlugField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
