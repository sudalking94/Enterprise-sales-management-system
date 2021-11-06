import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from enterprise.models import Enterprise, EnterpriseAccessLog
import rstr


class Command(BaseCommand):

    help = "This command creates user agents"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many user agents you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        enterprises = Enterprise.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(EnterpriseAccessLog, number, {
            "enterprise": lambda x: random.choice(enterprises),
            "agent": lambda x: seeder.faker.user_agent(),
            "ip": lambda x: rstr.xeger('(\d{3}\.){3}\d{2}'),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} user agents created!"))
