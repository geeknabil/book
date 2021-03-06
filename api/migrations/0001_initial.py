# Generated by Django 4.0.3 on 2022-03-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('synopsis', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
