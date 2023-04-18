# Generated by Django 4.2 on 2023-04-18 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comment', to='main_app.comment')),
                ('author_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to='main_app.post')),
                ('author_topic', models.ManyToManyField(to='main_app.topic')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='post',
            name='author_topic',
            field=models.ManyToManyField(to='main_app.topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='main_app.post'),
        ),
    ]
