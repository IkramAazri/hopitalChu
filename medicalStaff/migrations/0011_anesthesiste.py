# Generated by Django 3.0.5 on 2020-05-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0010_auto_20200509_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anesthesiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('prenom', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
