# Generated by Django 2.1.2 on 2018-11-27 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0010_auto_20181127_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='quiz.Answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_answers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='student',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='students',
            field=models.ManyToManyField(related_name='join_quiz', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TakenQuiz',
        ),
    ]
