import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """디렉토리에 존재하는 모든 파이캐시 파일을 지움"""

    def handle(self, *args, **options):
        remove_pycache = 'find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf'
        os.system(remove_pycache)
