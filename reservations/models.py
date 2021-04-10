from django.db import models
from core import models as core_models


# Create your models here.
class Reservation(core_models.TimeStampedModel):

    """Reservation Model Defination"""

    STATUS_PENDING = "pending"
    STATUS_COMFIRMED = "confirmed"
    STATUS_CANCELLED = "canceled"

    STATUD_CHOICES = (
        (STATUS_PENDING, "Pedning"),
        (STATUS_COMFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUD_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
