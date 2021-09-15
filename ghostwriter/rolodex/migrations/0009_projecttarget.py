# Generated by Django 3.0.10 on 2021-02-02 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0008_projectscope'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(help_text="Enter the target's IP address", unique=True, verbose_name='IP Address')),
                ('hostname', models.CharField(blank=True, help_text="Provide the target's hostname or fully qualified domain name", max_length=255, null=True, verbose_name='Hostname / FQDN')),
                ('note', models.TextField(blank=True, help_text='Provide a list of IP addresses, ranges, hostnames, or a mix with each entry on a new line', null=True, verbose_name='Scope')),
                ('compromised', models.BooleanField(default=False, help_text='Flag this host as compromised', verbose_name='Compromised')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rolodex.Project')),
            ],
            options={
                'verbose_name': 'Project target',
                'verbose_name_plural': 'Project targets',
                'ordering': ['project', 'compromised', 'ip_address', 'hostname'],
            },
        ),
    ]