import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from enterprise.models import Enterprise
from customer.models import Customer
from product.models import Product, SalesLog


class Command(BaseCommand):

    help = "This command creates sales logs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many sales logs you want to create"
        )

    def handle(self, *args, **options):
        enterprises = Enterprise.objects.all()
        customers = Customer.objects.all()
        products = Product.objects.all()

        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(SalesLog, number, {
            "enterprise": lambda x: random.choice(enterprises),
            "customer": lambda x: random.choice(customers),
            "product": lambda x: random.choice(products),
        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} sales logs created!"))
