# Generated by Django 4.1.7 on 2023-03-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_curs_post_curs_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Post/Fil', verbose_name='Файл'),
        ),
    ]
