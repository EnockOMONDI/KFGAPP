# Generated by Django 3.2.20 on 2025-01-21 21:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_editpage_section_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editpage',
            name='heading',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
