# Generated by Django 3.0.6 on 2020-07-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerapp', '0007_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnOnInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=250)),
                ('multiplier', models.IntegerField(default=0)),
                ('info', models.TextField()),
            ],
        ),
    ]
