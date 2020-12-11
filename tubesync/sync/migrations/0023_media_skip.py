# Generated by Django 3.1.4 on 2020-12-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0022_auto_20201211_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='skip',
            field=models.BooleanField(db_index=True, default=False, help_text='Media will be skipped and not downloaded', verbose_name='skip'),
        ),
    ]