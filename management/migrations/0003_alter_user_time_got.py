# Generated by Django 5.1.2 on 2024-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_user_time_got'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_got',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
