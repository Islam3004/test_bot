# Generated by Django 3.2.9 on 2022-04-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Word')),
                ('gender', models.CharField(choices=[('der', 'Der'), ('die', 'Die'), ('das', 'Das')], max_length=3, verbose_name='Gender')),
            ],
        ),
    ]
