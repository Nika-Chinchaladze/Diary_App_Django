# Generated by Django 4.1.6 on 2023-04-09 10:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_based_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name': 'Diary'},
        ),
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
