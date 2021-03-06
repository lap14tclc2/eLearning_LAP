# Generated by Django 2.1.2 on 2018-11-27 03:08

from django.db import migrations, models

from django.utils.timezone import now
class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=64, verbose_name="Quiz's name"),
        ),
    ]
