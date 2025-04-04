# Generated by Django 5.1.6 on 2025-02-11 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("debate_arena", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DebatePrioritization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "ranking_score",
                    models.FloatField(
                        help_text="Computed ranking score for the debate"
                    ),
                ),
                (
                    "criteria",
                    models.JSONField(
                        blank=True,
                        help_text="JSON data detailing the ranking criteria",
                        null=True,
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Additional notes or rationale for the ranking",
                        null=True,
                    ),
                ),
                (
                    "debate_session",
                    models.ForeignKey(
                        help_text="Debate session being ranked",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prioritizations",
                        to="debate_arena.debatesession",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
