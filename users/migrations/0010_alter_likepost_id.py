# Generated by Django 4.0.4 on 2022-05-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_post_liked_alter_likepost_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
