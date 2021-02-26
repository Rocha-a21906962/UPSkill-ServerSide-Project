# Generated by Django 3.1.7 on 2021-02-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='dob',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='actor',
            name='pic',
            field=models.ImageField(blank=True, upload_to='actor/%Y/%m/%d/'),
        ),
    ]