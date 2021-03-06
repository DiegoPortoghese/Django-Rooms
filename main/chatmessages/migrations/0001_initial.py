# Generated by Django 3.0 on 2019-12-20 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0020_auto_20191219_1909'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('displayed', models.BooleanField(default=False, verbose_name='Visualizzato')),
                ('from_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('room_ref', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room_ref', to='rooms.Room')),
                ('to_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
