import os
import requests
from django.core.cache import cache

class TransparencyTokenService:
    TOKEN_URL = (
        "https://api2.transparencia.rr.gov.br/"
        "transparencia/oauth/token?grant_type=client_credentials"
    )

    @staticmethod
    def get_acess_token() -> str:
        token = cache.get("acess_token_api")

        if not token:
            return TransparencyTokenService.refresh_token()

        return token



    @staticmethod
    def refresh_token() -> str:

        username = os.environ.get("API_USERNAME")
        password = os.environ.get("API_PASSWORD")

        if not username or not password:
            raise RuntimeError("invalid credentials api")

        response = requests.post(TransparencyTokenService.TOKEN_URL, auth=(username, password), timeout=10)
        response.raise_for_status()

        data = response.json()

        return data["access_token"]

