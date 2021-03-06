# Generated by Django 2.2.6 on 2020-04-06 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('userlogin', models.CharField(max_length=45)),
                ('avartar_url', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Repos',
            fields=[
                ('repo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('reponame', models.CharField(max_length=150)),
                ('owner', models.CharField(max_length=45)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attendance.User')),
            ],
            options={
                'db_table': 'repos',
            },
        ),
    ]
