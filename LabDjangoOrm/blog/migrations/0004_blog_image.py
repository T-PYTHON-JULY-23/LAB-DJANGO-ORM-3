# Generated by Django 4.2.4 on 2023-08-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='img/def.jpg', upload_to='img/'),
            preserve_default=False,
        ),
    ]
