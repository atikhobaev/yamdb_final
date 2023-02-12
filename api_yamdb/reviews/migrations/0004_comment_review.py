# Generated by Django 2.2.16 on 2022-11-08 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221105_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Отзыв'),
        ),
    ]
