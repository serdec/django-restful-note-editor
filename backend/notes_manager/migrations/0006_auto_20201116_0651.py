# Generated by Django 3.1.3 on 2020-11-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_manager', '0005_auto_20201116_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]