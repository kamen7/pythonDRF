# Generated by Django 3.2 on 2021-12-29 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=50)),
                ('flat', models.IntegerField(max_length=10)),
                ('zip_code', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='Address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contacts.address'),
        ),
    ]