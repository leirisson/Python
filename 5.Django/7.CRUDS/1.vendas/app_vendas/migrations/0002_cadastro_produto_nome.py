# Generated by Django 5.1.1 on 2024-09-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_produto',
            name='nome',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]