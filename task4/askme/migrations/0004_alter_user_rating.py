# Generated by Django 4.1.7 on 2023-04-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0003_alter_answer_author_alter_answer_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='rating'),
        ),
    ]
