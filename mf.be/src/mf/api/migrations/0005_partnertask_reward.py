# Generated by Django 5.1.1 on 2024-12-04 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_partnertask_name_alter_partnertask_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnertask',
            name='reward',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]