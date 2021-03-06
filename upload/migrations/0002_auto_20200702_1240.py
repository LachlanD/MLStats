# Generated by Django 3.0.8 on 2020-07-02 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='upload.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='upload.Song')),
                ('submitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='upload.User')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.AddField(
            model_name='vote',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Week'),
        ),
        migrations.AddField(
            model_name='song',
            name='submitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='upload.User'),
        ),
        migrations.AddField(
            model_name='song',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Week'),
        ),
    ]
