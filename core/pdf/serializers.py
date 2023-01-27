from rest_framework import serializers
from core.user.models import PDF
from rest_framework.response import Response
from rest_framework import status


class PDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PDF
        fields = ['id', 'name', 'pdf']
