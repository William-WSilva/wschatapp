# Generated by Django 4.2.7 on 2023-11-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wschatapp", "0003_alter_post_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="imagem",
            field=models.ImageField(blank=True, upload_to="imagem/%Y/%m/%d/"),
        ),
    ]