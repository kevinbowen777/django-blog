# Generated by Django 4.2.1 on 2023-06-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("PB", "Published")],
                default="PB",
                max_length=2,
            ),
        ),
    ]
