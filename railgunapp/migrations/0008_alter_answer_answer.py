# Generated by Django 4.0.5 on 2025-01-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railgunapp', '0007_post_slogan_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
