from django.core.cache import cache
from django.core.management import BaseCommand
from website.services.transparency_token import TransparencyTokenService

class Command(BaseCommand):
    help = "Posts auth token"
    def handle(self, *args, **options):
        self.stdout.write("Posting auth token...")

        token = TransparencyTokenService.get_acess_token()
        cache.set("acess_token_api", token, timeout=3500)
        self.stdout.write(self.style.SUCCESS("Successfully posted auth token"))
        self.stdout.write(token)