from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Site(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} - {self.name}"


class SourceSystem(models.Model):
    SOURCE_TYPES = [
        ("sap", "SAP"),
        ("utility", "Utility"),
        ("travel", "Travel"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    source_type = models.CharField(max_length=50, choices=SOURCE_TYPES)

    def __str__(self):
        return self.name


class IngestionRun(models.Model):
    source_system = models.ForeignKey(SourceSystem, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="processing")
    total_rows = models.IntegerField(default=0)
    failed_rows = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class RawRecord(models.Model):
    ingestion_run = models.ForeignKey(IngestionRun, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    raw_payload = models.JSONField()
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Raw Row {self.row_number}"


class ActivityRecord(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("suspicious", "Suspicious"),
        ("failed", "Failed"),
        ("approved", "Approved"),
        ("locked", "Locked"),
    ]

    SCOPE_CHOICES = [
        ("scope_1", "Scope 1"),
        ("scope_2", "Scope 2"),
        ("scope_3", "Scope 3"),
    ]

    raw_record = models.OneToOneField(RawRecord, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)

    activity_type = models.CharField(max_length=100)
    scope = models.CharField(max_length=50, choices=SCOPE_CHOICES)

    activity_date = models.DateField(null=True, blank=True)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)

    quantity_original = models.FloatField(null=True, blank=True)
    unit_original = models.CharField(max_length=50, blank=True)

    quantity_normalized = models.FloatField(null=True, blank=True)
    unit_normalized = models.CharField(max_length=50, blank=True)

    emissions_kgco2e = models.FloatField(null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    flags = models.JSONField(default=list)

    locked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.status}"


class ReviewDecision(models.Model):
    activity_record = models.ForeignKey(ActivityRecord, on_delete=models.CASCADE)
    decision = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.decision


class AuditEvent(models.Model):
    activity_record = models.ForeignKey(ActivityRecord, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_type