# Generated by Django 3.1.3 on 2020-11-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_manager', '0004_auto_20201116_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
