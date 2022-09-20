from dataclasses import field
from rest_framework import serializers
from contents.models import HostedContent
from contents.models import UploadedContent
from contents.models import CheckedContent



class HostedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostedContent
        fields = '__all__'


class UploadedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedContent
        fields = '__all__'


class CheckedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckedContent
        fields = '__all__'
