# Generated by Django 4.2.4 on 2023-08-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_upload',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
