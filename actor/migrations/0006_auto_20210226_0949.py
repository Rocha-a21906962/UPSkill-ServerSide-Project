# Generated by Django 3.1.7 on 2021-02-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0005_auto_20210226_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='dob',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]