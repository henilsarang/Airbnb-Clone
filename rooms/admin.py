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

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Space",
            {
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "count_amenities",
    )

    list_filter = (
        "city",
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()
