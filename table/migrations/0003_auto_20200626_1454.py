# Generated by Django 3.0.7 on 2020-06-26 05:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table', '0002_auto_20200626_1454'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notice2Table',
            new_name='NoticeTable',
        ),
    ]