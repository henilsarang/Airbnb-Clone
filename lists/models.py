from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    """List model Defination"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.room", blank=True)

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number Of Rooms"

    def __str__(self):
        return self.name