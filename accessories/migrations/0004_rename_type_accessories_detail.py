# Generated by Django 5.0.1 on 2024-03-17 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0003_tag_accessories_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessories',
            old_name='type',
            new_name='detail',
        ),
    ]
