# Generated by Django 3.1.3 on 2021-04-25 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0002_finalorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalorder',
            name='name',
            field=models.CharField(default='Reverend_Manuel', max_length=100),
            preserve_default=False,
        ),
    ]
