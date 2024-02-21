# Generated by Django 4.2.4 on 2024-02-21 09:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('POP', 'Pop Music'), ('JAZZ', 'Jazz Music'), ('R&B', 'R&B Music'), ('ROCK', 'Rock Music'), ('COUNTRY', 'Country Music'), ('DANCE', 'Dance Music'), ('HIPHOP', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='profiles.profile')),
            ],
        ),
    ]
