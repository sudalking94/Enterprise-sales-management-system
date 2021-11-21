import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from customer.models import Customer, Group
from enterprise.models import Enterprise


class Command(BaseCommand):

    help = "This command creates products"

    class GroupWithEnterprise:
        def set_enterprise(self, enterprise):
            self.enterprise = enterprise

        def get_enterprise(self):
            return self.enterprise

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many customers you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        enterprises = Enterprise.objects.all()
        group = Group.objects

        seeder = Seed.seeder()
        seed_group = self.GroupWithEnterprise()

        def get_random_enterprise(list):
            result = random.choice(list)
            seed_group.set_enterprise(result)
            return result

        seeder.add_entity(Customer, number, {
            "enterprise": lambda x: get_random_enterprise(enterprises),
            "name": lambda x: seeder.faker.name(),
            "group": lambda x: random.choice(group.filter(enterprise=seed_group.get_enterprise())),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} customers created!"))
