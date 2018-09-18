# Generated by Django 2.1.1 on 2018-09-18 13:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='Invalid Cellphone Number', message='Cellphone Number format [09xxxxxxxxx].', regex='(09)\\d{9}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]