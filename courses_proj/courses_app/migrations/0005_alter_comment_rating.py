# Generated by Django 3.2.3 on 2021-05-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_auto_20210530_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐⭐')], default=1, max_length=5, null=True),
        ),
    ]
