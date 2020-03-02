# Generated by Django 2.2.10 on 2020-02-28 13:28

from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('position', positions.fields.PositionField(default=-1)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.Topic')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
