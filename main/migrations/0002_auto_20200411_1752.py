# Generated by Django 3.0.5 on 2020-04-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_availibility',
            field=models.CharField(choices=[('T', 'Availible'), ('F', 'Not availible')], default='T', max_length=20),
        ),
    ]
