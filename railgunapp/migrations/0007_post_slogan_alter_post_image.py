# Generated by Django 4.0.5 on 2025-01-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railgunapp', '0006_alter_post_background_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slogan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
