# Generated by Django 5.1.1 on 2024-12-03 11:30

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_options_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.task')),
                ('name', models.CharField(verbose_name=builtins.min)),
                ('url', models.URLField(max_length=100)),
            ],
            bases=('api.task',),
        ),
    ]