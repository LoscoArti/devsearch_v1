# Generated by Django 4.1.1 on 2022-10-27 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
