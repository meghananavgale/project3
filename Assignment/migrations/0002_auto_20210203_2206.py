# Generated by Django 3.1.6 on 2021-02-03 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password2',
        ),
    ]