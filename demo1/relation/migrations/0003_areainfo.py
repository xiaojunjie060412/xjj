# Generated by Django 2.2.2 on 2019-06-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relation.AreaInfo')),
            ],
        ),
    ]
