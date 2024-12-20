# Generated by Django 5.1.1 on 2024-11-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_year', models.IntegerField()),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('poster_url', models.URLField()),
            ],
        ),
    ]
