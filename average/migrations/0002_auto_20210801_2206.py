# Generated by Django 3.2.5 on 2021-08-01 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210801_2042'),
        ('portfolio', '0005_auto_20210801_2042'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('average', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Average',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='average', to='user.field')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='average', to='portfolio.business')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='average', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
