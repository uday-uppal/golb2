# Generated by Django 5.0.6 on 2024-06-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.CharField(default='Purple Penguin', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.CharField(max_length=10000000),
        ),
    ]
