# Generated by Django 2.2.3 on 2019-08-28 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0002_objectivestatus_projectobjective'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectobjective',
            options={'ordering': ['project', 'complete', 'deadline', 'status', 'objective'], 'verbose_name': 'Project objective', 'verbose_name_plural': 'Project objectives'},
        ),
    ]