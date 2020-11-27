# Generated by Django 3.1.3 on 2020-11-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=14)),
                ('guaranteed_compensation', models.DecimalField(decimal_places=2, max_digits=14)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.club')),
                ('positions', models.ManyToManyField(to='players.Position')),
            ],
        ),
    ]
