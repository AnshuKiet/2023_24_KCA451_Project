# Generated by Django 5.0.1 on 2024-04-24 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeScanner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumescanner',
            old_name='feedback',
            new_name='resume_feedback',
        ),
        migrations.RenameField(
            model_name='resumescanner',
            old_name='field_choice',
            new_name='resume_type',
        ),
    ]