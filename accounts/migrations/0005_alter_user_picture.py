# Generated by Django 4.1.1 on 2022-10-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_options_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='images/default_pic.png', null=True, upload_to=''),
        ),
    ]
