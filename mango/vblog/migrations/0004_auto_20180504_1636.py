# Generated by Django 2.0.2 on 2018-05-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0003_auto_20180504_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('tag', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=1000)),
                ('author', models.CharField(blank=True, max_length=20)),
                ('add_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_content',
                'ordering': ['-add_time'],
            },
        ),
        migrations.DeleteModel(
            name='BlogContent',
        ),
        migrations.AddIndex(
            model_name='content',
            index=models.Index(fields=['content'], name='tb_content_content_79b958_idx'),
        ),
    ]
