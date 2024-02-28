from django.db import models
from portfolio.models import Portfolio
from order.models import OrderBy


class OrderItem(models.Model):
    order = models.ForeignKey(
            OrderBy,
            on_delete=models.CASCADE,
            related_name="items"
            )
    product = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"product item {self.id} for Order {self.order.id}"
