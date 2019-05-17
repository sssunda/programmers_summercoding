# Generated by Django 2.0.13 on 2019-05-16 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='complete_chk',
            field=models.BooleanField(default=False, verbose_name='완료 여부'),
        ),
        migrations.AlterField(
            model_name='post',
            name='due_date',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True, verbose_name='마감기한'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rank',
            field=models.CharField(max_length=3, verbose_name='우선 순위'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]