# Generated by Django 4.2.3 on 2023-09-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
