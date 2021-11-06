import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from customer.models import Customer, Group
from enterprise.models import Enterprise


class Command(BaseCommand):

    help = "This command creates products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many customers you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        enterprises = Enterprise.objects.all()
        group = Group.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(Customer, number, {
            "enterprise": lambda x: random.choice(enterprises),
            "name": lambda x: seeder.faker.name(),
            "group": lambda x: random.choice(group),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} customers created!"))
