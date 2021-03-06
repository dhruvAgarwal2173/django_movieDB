# Generated by Django 2.2.4 on 2020-04-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the movie title', max_length=150, unique=True)),
                ('genre', models.CharField(help_text='Enter the genre', max_length=75)),
                ('release', models.DateField(help_text='Enter the initial release date')),
                ('rating', models.PositiveSmallIntegerField(help_text='Enter a value from 1 to 10')),
            ],
        ),
    ]
