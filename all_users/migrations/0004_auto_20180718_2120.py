# Generated by Django 2.0.2 on 2018-07-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_users', '0003_auto_20180718_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('candidate', 'Candidate'), ('employer', 'Employer')], default='candidate', max_length=50),
        ),
    ]
