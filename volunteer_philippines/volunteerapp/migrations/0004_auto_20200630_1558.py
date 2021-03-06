# Generated by Django 3.0.6 on 2020-06-30 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerapp', '0003_auto_20200630_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(max_length=150, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='volunteerapp.User'),
        ),
    ]
