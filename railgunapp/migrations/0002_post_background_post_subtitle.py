# Generated by Django 5.1.3 on 2024-12-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railgunapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background',
            field=models.FileField(null=True, upload_to='blog-post-image'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
