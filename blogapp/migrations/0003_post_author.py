# Generated by Django 3.2.20 on 2024-10-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Author',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]