# Generated by Django 4.0.2 on 2022-02-16 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_alter_house_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghost',
            name='house',
        ),
        migrations.AddField(
            model_name='house',
            name='ghost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.ghost'),
        ),
    ]
