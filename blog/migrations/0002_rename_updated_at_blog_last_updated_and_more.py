# Generated by Django 5.1.3 on 2024-11-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='updated_at',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='blog',
            name='comments_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
