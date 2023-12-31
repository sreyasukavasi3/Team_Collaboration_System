# Generated by Django 3.0.3 on 2020-02-21 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sentFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directFrom', to=settings.AUTH_USER_MODEL)),
                ('sentTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directTo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
