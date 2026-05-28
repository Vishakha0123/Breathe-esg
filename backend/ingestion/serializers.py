from rest_framework import serializers
from .models import ActivityRecord, IngestionRun

class IngestionRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngestionRun
        fields = "__all__"
class ActivityRecordSerializer(serializers.ModelSerializer):
    raw_payload=serializers.SerializerMethodField()
    site_code=serializers.SerializerMethodField()

    class Meta:
        model = ActivityRecord
        fields = "__all__"

    def get_raw_payload(self,obj):
        return obj.raw_record.raw_payload
    
    def get_site_code(self,obj):
        return obj.site.code if obj.site else None

    