from django.db import models
from events_app.models import Event

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.event.name} - {self.code}"
