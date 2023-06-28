# Generated by Django 4.2.2 on 2023-06-28 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(max_length=60)),
                ('desctription', models.CharField(max_length=200)),
                ('capital_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.capital')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_place', models.CharField(max_length=100)),
                ('description_place', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.country')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('data_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(max_length=6)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.user')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.currency'),
        ),
        migrations.AddField(
            model_name='country',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.language'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureTime.user')),
            ],
        ),
    ]
