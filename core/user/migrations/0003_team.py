# Generated by Django 4.1 on 2022-10-06 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.IntegerField()),
                ('is_team', models.BooleanField(default=False)),
                ('pseudo', models.CharField(max_length=255)),
                ('order', models.IntegerField(max_length=2)),
                ('lvl', models.IntegerField(max_length=2)),
                ('ability1', models.IntegerField(max_length=2)),
                ('ability2', models.IntegerField(max_length=2)),
                ('ability3', models.IntegerField(max_length=2)),
                ('ability4', models.IntegerField(max_length=2)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_user.game')),
            ],
        ),
    ]
