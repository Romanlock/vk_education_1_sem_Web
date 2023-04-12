# Generated by Django 4.1.7 on 2023-04-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0002_user_photo_alter_question_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(related_name='questions', to='askme.tag', verbose_name='Теги'),
        ),
    ]
