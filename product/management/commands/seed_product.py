import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from product.models import Product
from enterprise.models import Enterprise


class Command(BaseCommand):

    help = "This command creates products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many products you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        enterprises = Enterprise.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(Product, number, {
            "enterprise": lambda x: random.choice(enterprises)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} products created!"))
