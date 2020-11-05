# Generated by Django 3.0.10 on 2020-11-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandcenter', '0004_auto_20201028_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportconfiguration',
            name='label_figure',
            field=models.CharField(default='Figure', help_text='The label that comes before the figure number and caption in Word reports', max_length=255, verbose_name='Label Used for Figures'),
        ),
        migrations.AddField(
            model_name='reportconfiguration',
            name='label_table',
            field=models.CharField(default='Table', help_text='The label that comes before the table number and caption in Word reports', max_length=255, verbose_name='Label Used for Tables'),
        ),
        migrations.AlterField(
            model_name='reportconfiguration',
            name='prefix_figure',
            field=models.CharField(default='–', help_text='Unicode character to place between the label and your figure caption in Word reports', max_length=255, verbose_name='Character Before Figure Captions'),
        ),
        migrations.AlterField(
            model_name='reportconfiguration',
            name='prefix_table',
            field=models.CharField(default='–', help_text='Unicode character to place between the label and your table caption in Word reports', max_length=255, verbose_name='Character Before Table Titles'),
        ),
    ]
