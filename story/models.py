from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    UNIT_CHOICE = (
        (1, ("ml")),
        (2, ("g")),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    sku_number = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(default=0)
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.SET_NULL, blank=True, null=True)
    unit = models.PositiveIntegerField(choices=UNIT_CHOICE, default=1)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} — {self.quantity} {self.get_unit_display()}"
