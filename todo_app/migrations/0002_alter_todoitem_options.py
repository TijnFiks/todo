# Generated by Django 4.2.1 on 2023-06-28 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ['due_date']},
        ),
    ]
