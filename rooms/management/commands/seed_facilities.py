from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command seeds facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private Entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities added !"))
