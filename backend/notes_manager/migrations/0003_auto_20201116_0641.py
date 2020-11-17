# Generated by Django 3.1.3 on 2020-11-16 06:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes_manager', '0002_remove_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]