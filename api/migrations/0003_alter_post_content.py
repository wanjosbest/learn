# Generated by Django 5.1.1 on 2024-10-08 18:35

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(null=True, verbose_name='Text'),
        ),
    ]
