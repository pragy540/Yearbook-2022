# Generated by Django 4.0.1 on 2022-03-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook_app', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=750)),
            ],
        ),
    ]
