# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import WaterRecord

class WaterRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterRecord
        fields = ('id', 'waterName', 'released', 'releasedDate')