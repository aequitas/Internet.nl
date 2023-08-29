# Generated by Django 3.2.19 on 2023-08-04 08:55

import checks.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("checks", "0013_auto_20230517_1206"),
    ]

    operations = [
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="referrer_policy_errors",
            field=checks.models.ListField(default=[]),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="referrer_policy_recommendations",
            field=checks.models.ListField(default=[]),
        ),
    ]