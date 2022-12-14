# Generated by Django 4.0.6 on 2022-08-24 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(blank=True, max_length=225)),
                ('nature', models.CharField(max_length=225)),
                ('affect_gp', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=225)),
                ('nett_balance', models.CharField(max_length=225)),
                ('used_for', models.CharField(max_length=225)),
                ('method', models.CharField(max_length=225)),
                ('under', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.under')),
            ],
        ),
    ]
