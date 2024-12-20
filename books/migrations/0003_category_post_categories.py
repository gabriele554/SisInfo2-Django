# Generated by Django 5.1.1 on 2024-11-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='books.category'),
        ),
    ]
