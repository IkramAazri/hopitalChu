# Generated by Django 3.0.5 on 2020-05-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0008_auto_20200508_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='prenom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medecin',
            name='specialite',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='nom',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
