# Generated by Django 3.2.1 on 2021-11-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A', 'Thing'), ('O', 'Other')], db_index=True, max_length=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.group')),
            ],
        ),
    ]
