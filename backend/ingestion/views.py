from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .models import ActivityRecord,ReviewDecision, AuditEvent
from .serializers import ActivityRecordSerializer
from .services import ingest_csv

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_file(request):
    file=request.FILES.get("file")
    source_type=request.data.get("source_type")

    if not file:
        return Response({"error":"No file uploaded"},status=400)
    if source_type not in ["sap","utility","travel"]:
        return Response({"error":"Invalid source type"},status=400)
    
    run=ingest_csv(file, source_type)

    return Response({
        "id": run.id,
        "status": run.status,
        "total_rows": run.total_rows,
        "failed_rows": run.failed_rows,
    })

@api_view(["GET"])

def activities(request):
    status_filter=request.GET.get("status")

    records=ActivityRecord.objects.all().order_by("-created_at")

    if status_filter:
        records=records.filter(status=status_filter)
    
    serializer=ActivityRecordSerializer(records,many=True)

    return Response(serializer.data)

@api_view(["POST"])
def approve_activity(request, pk):

    activity = ActivityRecord.objects.get(pk=pk)

    if activity.status == "locked":
        return Response(
            {"error": "Record is already locked"},
            status=400
        )

    old_status = activity.status

    activity.status = "approved"
    activity.save()

    ReviewDecision.objects.create(
        activity_record=activity,
        decision="approved",
        comment=request.data.get("comment", "")
    )

    AuditEvent.objects.create(
        activity_record=activity,
        event_type="approved",
        details={
            "old_status": old_status,
            "new_status": "approved"
        }
    )

    return Response({"status": "approved"})

    return Response({"status":"approved"})

@api_view(["POST"])

def lock_activity(request,pk):
    activity=ActivityRecord.objects.get(pk=pk)

    if activity.status != "approved":
        return Response({"error":"Only approved records can be locked"},status=400)
    activity.status="locked"

    activity.locked_at=timezone.now()
    activity.save()

    AuditEvent.objects.create(
        activity_record=activity,
        event_type="locked",
        details={}
    )

    return Response({"status":"locked"})