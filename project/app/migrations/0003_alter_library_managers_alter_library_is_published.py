# Generated by Django 4.2.1 on 2023-10-11 17:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_library_publishing_date_library_is_published'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='library',
            managers=[
                ('custom_object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='library',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
