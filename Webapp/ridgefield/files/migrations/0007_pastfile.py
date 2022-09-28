# Generated by Django 4.1.1 on 2022-09-27 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0006_alter_file_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filedata', models.FileField(upload_to='files/')),
                ('replaced', models.DateTimeField(auto_now_add=True)),
                ('fileref', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='past_versions', to='files.file')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-replaced'],
            },
        ),
    ]
