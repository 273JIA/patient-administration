# Generated by Django 3.1.6 on 2022-02-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(default=False, verbose_name='User has this responsability')),
                ('user', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('option', models.CharField(choices=[('It happened to me', 'It happened to me'), ('It was already like that', 'It was already like that')], max_length=100)),
                ('reason', models.CharField(choices=[('Delete patient', 'Delete patient'), ('System problems', 'System problems'), ('Others', 'Others')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Situation', models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
