from django.contrib import admin

from .models import(
    Tenant,
    Site,
    SourceSystem,
    IngestionRun,
    RawRecord,
    ActivityRecord,
    ReviewDecision,
    AuditEvent,
)

admin.site.register(Tenant)
admin.site.register(Site)
admin.site.register(SourceSystem)
admin.site.register(IngestionRun)
admin.site.register(RawRecord)
admin.site.register(ActivityRecord)
admin.site.register(ReviewDecision)
admin.site.register(AuditEvent)
