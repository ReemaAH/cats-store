# Generated by Django 3.2.4 on 2021-06-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
