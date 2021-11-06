from django.core.management.base import BaseCommand
from django_seed import Seed
from enterprise.models import Enterprise
import rstr


class Command(BaseCommand):

    help = "This command creates enterprises"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many enterprises you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(Enterprise, number, {
            "is_staff": False,
            "is_superuser": False,
            "b_no": lambda x: rstr.xeger('\d{3}-\d{2}-\d{5}'),
            "name": lambda x: seeder.faker.company(),
        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} enterprises created!"))
