import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from enterprise.models import Enterprise
from customer.models import Customer
from product.models import Product, SalesLog


class Command(BaseCommand):

    help = "This command creates sales logs"

    class Price:
        def setPrice(self, price):
            self.price = price

        def getPrice(self):
            return self.price

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

        SeedPrice = self.Price()

        def get_random_price(list):
            result = random.choice(list)
            SeedPrice.setPrice(result.price)
            return result

        seeder.add_entity(SalesLog, number, {
            "enterprise": lambda x: random.choice(enterprises),
            "customer": lambda x: random.choice(customers),
            "product": lambda x: get_random_price(products),
            "price": lambda x: SeedPrice.getPrice(),
        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} sales logs created!"))
