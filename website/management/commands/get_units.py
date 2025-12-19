
from django.core.management.base import BaseCommand, CommandError
from website.services.transparency_token import TransparencyTokenService
from website.services.transparency_units import TransparencyUnitService

class Command(BaseCommand):
    help = "Get units budgetary in API Fiplan"

    def handle(self, *args, **options):
        self.stdout.write("Getting units budgetary...")

        token = TransparencyTokenService.get_acess_token()

        TransparencyUnitService.get_transparency_units(token)

        self.stdout.write(self.style.SUCCESS("Successfully get units"))
