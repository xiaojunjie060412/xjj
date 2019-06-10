# Generated by Django 2.2.2 on 2019-06-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=20),
        ),
    ]