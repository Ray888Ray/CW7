# Generated by Django 4.1.4 on 2022-12-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.CharField(max_length=20, verbose_name='Survey')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded')),
            ],
        ),
        migrations.DeleteModel(
            name='First',
        ),
    ]
