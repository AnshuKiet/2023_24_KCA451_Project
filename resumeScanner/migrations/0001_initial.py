# Generated by Django 5.0.1 on 2024-04-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeScanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_choice', models.CharField(choices=[('MERN', 'MERN'), ('JAVA', 'JAVA'), ('Python', 'Python'), ('Full Stack', 'Full Stack')], max_length=50)),
                ('resume_file', models.FileField(upload_to='resumes/')),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
    ]