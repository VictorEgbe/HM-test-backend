# Generated by Django 4.2.1 on 2023-12-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sector',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='sectors',
            field=models.ManyToManyField(to='sectors.sector'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
