# Generated by Django 4.2.4 on 2023-08-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_category_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
    ]
