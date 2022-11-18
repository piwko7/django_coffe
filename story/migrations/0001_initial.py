# Generated by Django 4.1.3 on 2022-11-07 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("supplier", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("sku_number", models.CharField(max_length=50)),
                ("quantity", models.IntegerField(default=0)),
                ("unit", models.PositiveIntegerField(choices=[(1, "ml"), (2, "g")], default=1)),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="supplier.supplier"
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]