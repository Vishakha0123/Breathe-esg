import csv

from ingestion.models import(
    Tenant,
    Site,
    SourceSystem,
    IngestionRun,
    RawRecord,
    ActivityRecord,
    AuditEvent,
)
from ingestion.parsers import sap_parser,utility_parser,travel_parser

PARSERS={
    "sap":sap_parser,
    "utility":utility_parser,
    "travel":travel_parser,
}

def ingest_csv(file,source_type):
    tenant = Tenant.objects.first()
    source = SourceSystem.objects.filter(source_type=source_type).first()

    run = IngestionRun.objects.create(
        source_system=source,
        file_name=file.name,
        status="processing"
    )

    decoded_file=file.read().decode("utf-8").splitlines()
    reader=csv.DictReader(decoded_file)

    total_rows=0
    failed_rows=0

    parser = PARSERS[source_type]
    for index, row in enumerate(reader,start=1):
        total_rows += 1

        raw_record=RawRecord.objects.create(
            ingestion_run=run,
            row_number=index,
            raw_payload=row
        )
        try:
            parsed=parser.parse(row)
            site=None

            if parsed.get("site_code"):
                site=Site.objects.filter(tenant=tenant, code=parsed.get("site_code")).first()

                if not site:
                    parsed["flags"].append("Unknown site")

            status="suspicious" if parsed["flags"] else "pending"

            activity=ActivityRecord.objects.create(
                raw_record=raw_record,
                tenant=tenant,
                site=site,
                activity_type=parsed["activity_type"],
                scope=parsed["scope"],
                activity_date=parsed.get("activity_date"),
                period_start=parsed.get("period_start"),
                period_end=parsed.get("period_end"),
                quantity_original=parsed.get("quantity_original"),
                unit_original=parsed.get("unit_original"),
                quantity_normalized=parsed.get("quantity_normalized"),
                unit_normalized=parsed.get("unit_normalized"),
                emissions_kgco2e=parsed.get("emissions_kgco2e"),
                flags=parsed["flags"],
                status=status,
            )

            AuditEvent.objects.create(
                activity_record=activity,
                event_type="created_from_ingestion",
                details={
                    "source_type":source_type,
                    "file_name":file.name,
                    "row_number":index,
                }
            )

        except Exception as e:
            failed_rows+=1
            raw_record.error=str(e)
            raw_record.save()

    run.total_rows=total_rows
    run.failed_rows=failed_rows
    run.status="completed"
    run.save()

    return run

                
