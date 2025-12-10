import os

import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Posts auth token"
    def handle(self, *args, **options):
        self.stdout.write("Posting auth token...")

        url = "https://api2.transparencia.rr.gov.br/transparencia/oauth/token?grant_type=client_credentials"
        response = requests.post(url, auth=("integracao_geral", "agtTAG57732#@#"))
        body = response.json()
        print(body["access_token"])