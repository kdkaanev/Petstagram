# Generated by Django 5.0.1 on 2024-01-31 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0007_alter_petphoto_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='photos.petphoto')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes', to='photos.petphoto')),
            ],
        ),
    ]
