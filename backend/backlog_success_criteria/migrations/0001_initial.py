# Generated by Django 5.1.1 on 2024-10-02 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("backlog", "0002_alter_backlog_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BacklogSuccessCriteria",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("successCriteria", models.TextField()),
                (
                    "backlog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="success_criteria",
                        to="backlog.backlog",
                    ),
                ),
            ],
            options={
                "db_table": "backlog_success_criteria",
            },
        ),
    ]