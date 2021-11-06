import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from enterprise.models import Enterprise
from customer.models import Group


class Command(BaseCommand):

    help = "This command creates groups"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many groups you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        enterprises = Enterprise.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(Group, number, {
            "enterprise": lambda x: random.choice(enterprises)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} products created!"))
