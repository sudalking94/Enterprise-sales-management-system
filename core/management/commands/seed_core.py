from django.core.management.base import BaseCommand
from enterprise.management.commands.seed_enterprise import Command as enterprise_command
from enterprise.management.commands.seed_access_log import Command as access_log_command
from customer.management.commands.seed_group import Command as group_command
from customer.management.commands.seed_customer import Command as customer_command
from product.management.commands.seed_product import Command as product_command
from product.management.commands.seed_sales_log import Command as sales_log_command


class Command(BaseCommand):
    """테스트 데이터를 전부 차례대로 저장"""

    help = "This command creates all models"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many you want to create"
        )

    def handle(self, *args, **options):
        ##enterprise_command.handle(self, *args, **options)
        product_command.handle(self, *args, **options)
        group_command.handle(self, *args, **options)
        customer_command.handle(self, *args, **options)
        access_log_command.handle(self, *args, **options)
        sales_log_command.handle(self, *args, **options)
