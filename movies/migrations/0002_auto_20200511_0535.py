# Generated by Django 2.1.5 on 2020-05-11 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='number_im_stock',
            new_name='number_in_stock',
        ),
    ]
