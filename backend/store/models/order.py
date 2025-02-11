from django.db import models
from .user import User
import uuid

class Order():
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_cod = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)