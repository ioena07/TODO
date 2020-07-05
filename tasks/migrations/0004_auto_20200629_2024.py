# Generated by Django 3.0 on 2020-06-29 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200629_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tasks.Category'),
        ),
    ]