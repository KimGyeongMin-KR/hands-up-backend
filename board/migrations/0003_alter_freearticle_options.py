# Generated by Django 4.1.3 on 2022-12-13 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_freearticle_hits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freearticle',
            options={'ordering': ['-id']},
        ),
    ]
