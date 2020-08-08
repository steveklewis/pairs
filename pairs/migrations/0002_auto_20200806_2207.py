# Generated by Django 3.1 on 2020-08-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
                ('slug', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='emotion',
            name='tags',
            field=models.ManyToManyField(related_name='emotions', to='pairs.Tag'),
        ),
        migrations.AddField(
            model_name='emotionpair',
            name='tags',
            field=models.ManyToManyField(related_name='pairs', to='pairs.Tag'),
        ),
    ]
