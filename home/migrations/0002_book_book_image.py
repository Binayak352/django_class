# Generated by Django 3.1.2 on 2020-10-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/book'),
        ),
    ]
