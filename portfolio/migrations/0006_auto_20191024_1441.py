# Generated by Django 2.2.6 on 2019-10-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20191024_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='category_name',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='cert_category',
            new_name='Category',
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(),
        ),
    ]
