# Generated by Django 5.1.1 on 2024-12-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_task_partnertask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnertask',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='partnertask',
            name='url',
            field=models.URLField(),
        ),
    ]