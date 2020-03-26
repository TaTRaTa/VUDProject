# Generated by Django 3.0.4 on 2020-03-23 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelpRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('title', models.SlugField()),
                ('expected_ppl_cnt', models.PositiveSmallIntegerField(default=0)),
                ('confirmed_ppl_cnt', models.PositiveSmallIntegerField(default=0)),
                ('rejected_pll_cnt', models.PositiveSmallIntegerField(default=0)),
                ('onhold_ppl_cnt', models.PositiveSmallIntegerField(default=0)),
                ('valid_days', models.PositiveSmallIntegerField(default=7)),
                ('isopen', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='VUD.Cities')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelpResponces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('isValid', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='VUD.Status')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='VUD.HelpRequests')),
            ],
        ),
        migrations.CreateModel(
            name='HelpRequestsDetail',
            fields=[
                ('postid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='VUD.HelpRequests')),
                ('description', models.TextField(max_length=500, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('Facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('email', models.URLField(null=True)),
                ('clinics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='VUD.Clinics')),
            ],
        ),
    ]
