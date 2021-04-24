from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command seeds amenities"

    def handle(self, *args, **options):
        amenities = [
            "Air conditining",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bad Lilen",
            "Boating",
            "Cable TV",
            "Carbon Monoxide Detectors",
            "Chairs",
            "Children Area",
            "Coffee Makes In The Room",
            "Cooking Hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double Bed",
            "En Suite Bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge/ Freezer",
            "Golf",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Oven",
            "Queen Size Bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke Detectors",
            "SOfa",
            "Stereo",
            "Swimming Pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created !!"))