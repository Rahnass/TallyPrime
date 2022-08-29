# Generated by Django 4.1 on 2022-08-29 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0017_remove_ledger_l_sundry_remove_ledger_l_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='l_tax_register',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_banking_details',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_mailing_address',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_rounding',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_satutory',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_sundry',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AlterField(
            model_name='ledger_tax',
            name='ledger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
    ]