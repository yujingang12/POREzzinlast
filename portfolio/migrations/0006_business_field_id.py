# Generated by Django 3.2.6 on 2021-08-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210801_2042'),
        ('portfolio', '0005_auto_20210801_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='field_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='user.field'),
        ),
    ]
