import os

import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Posts auth token"
    def handle(self, *args, **options):
        self.stdout.write("Posting auth token...")

        api_username = os.environ.get("API_USERNAME")
        api_password = os.environ.get("API_PASSWORD")
        url = "https://api2.transparencia.rr.gov.br/transparencia/oauth/token?grant_type=client_credentials"
        response = requests.post(url, auth=(api_username, api_password))
        body = response.json()
        return body["access_token"]