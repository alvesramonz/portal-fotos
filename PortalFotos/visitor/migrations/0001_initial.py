# Generated by Django 2.1.1 on 2020-11-16 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
                ('allowed', models.BooleanField(default=False)),
            ],
        ),
    ]