# Generated by Django 5.1.6 on 2025-02-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_agent', '0003_promptrequest_cc_promptrequest_signature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promptrequest',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
