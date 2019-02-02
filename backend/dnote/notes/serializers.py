# 모델을 참조하여 serializing
from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("id", "text")