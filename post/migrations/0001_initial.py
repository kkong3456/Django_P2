# Generated by Django 3.2.8 on 2021-10-11 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('dsuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
                ('img_url', models.CharField(max_length=256, verbose_name='이미지주소')),
                ('contents', models.TextField(verbose_name='내용')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('tags', models.ManyToManyField(to='tag.Tag', verbose_name='태그')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsuser.dsuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글',
                'db_table': 'djangostagram_post',
            },
        ),
    ]
