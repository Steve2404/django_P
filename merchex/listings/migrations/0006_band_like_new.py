# Generated by Django 5.0.6 on 2024-08-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]