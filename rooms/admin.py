from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definations"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Defination"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    "Room Admin Defination"

    pass