# Generated by Django 4.0.4 on 2022-05-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_likepost_like_remove_post_comment_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]