# Generated by Django 2.2.2 on 2019-06-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('choice1', models.CharField(max_length=20)),
                ('choice2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Problem')),
            ],
        ),
    ]