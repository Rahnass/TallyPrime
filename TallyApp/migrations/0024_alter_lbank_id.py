# Generated by Django 4.1 on 2022-08-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0023_alter_lbank_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lbank',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
