# Generated by Django 5.1.6 on 2025-02-05 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template_agent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promptrequest',
            old_name='user',
            new_name='created_by',
        ),
    ]
