# Generated by Django 4.1.5 on 2023-01-31 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['update', 'create']},
        ),
    ]
