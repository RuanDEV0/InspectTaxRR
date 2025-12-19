import os
import requests
from django.core.cache import cache

class TransparencyUnitService:
    URL = "https://api2.transparencia.rr.gov.br/transparencia/api/v1/unidades-orcamentarias"
    @staticmethod
    def get_transparency_units(token):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(TransparencyUnitService.URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return None
        else:
            return "erro na requisição"