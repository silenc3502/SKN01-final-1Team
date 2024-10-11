# Generated by Django 5.1.1 on 2024-10-11 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('report_team', '0002_resultreportteam_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultReportTeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=64)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to='report_team.resultreportteam')),
            ],
            options={
                'db_table': 'report_team_member',
            },
        ),
    ]