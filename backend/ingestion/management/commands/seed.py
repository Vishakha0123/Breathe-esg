from django.core.management.base import BaseCommand
from ingestion.models import Tenant,Site,SourceSystem

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        tenant, _ = Tenant.objects.get_or_create(
            name="Demo Enterprise Client"
        )
        Site.objects.get_or_create(
            tenant=tenant,
            code="PLO1",
            name="Mumbai Plant"
        )
        Site.objects.get_or_create(
            tenant=tenant,
            code="PL02",
            name="Pune Warehouse"
        )
        SourceSystem.objects.get_or_create(
            tenant=tenant,
            name="SAP Fuel Export",
            source_type="sap"
        )
        SourceSystem.objects.get_or_create(
            tenant=tenant,
            name="Utility Bill Export",
            source_type="utility"
        )
        SourceSystem.objects.get_or_create(
            tenant=tenant,
            name="Travel Expense Export",
            source_type="travel"
        )
        self.stdout.write(self.style.SUCCESS("Seed data created"))