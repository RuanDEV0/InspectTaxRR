import json
import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from website.models import Unit, Daily
from datetime import datetime
from decimal import Decimal

class Command(BaseCommand):
    help = "Get daily diaries in API Fiplan"

    def handle(self, *args, **options):
        self.stdout.write("Getting daily diaries...")
