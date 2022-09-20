from rest_framework.decorators import action
from rest_framework import response
from rest_framework import viewsets

from django.utils import timezone

from contents.models import (
    HostedContent,
    UploadedContent,
    CheckedContent
)
from contents.serializers import (
    HostedContentSerializer,
    UploadedContentSerializer,
    CheckedContentSerializer
)


class HostedContentViewSet(viewsets.ModelViewSet):
    serializer_class = HostedContentSerializer
    queryset = HostedContent.objects.all()


class UploadedContentViewSet(viewsets.ModelViewSet):
    serializer_class = UploadedContentSerializer
    queryset = UploadedContent.objects.all()

    @action(methods=["GET"], detail=False, url_path=r"hospital/(?P<hospital_id>[^/]+)/list")
    def by_hospital(self, *args, **kwargs):
        uploaded_contents_hospital = self.kwargs["hospital_id"]
        contents = UploadedContent.objects.filter(
            hospital__id=uploaded_contents_hospital)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)

    @action(methods=["GET"], detail=False, url_path=r"user/(?P<user_id>[^/]+)/list")
    def by_user(self, *args, **kwargs):
        uploaded_contents_user = self.kwargs["user_id"]
        contents = UploadedContent.objects.filter(
            users__id=uploaded_contents_user)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)

    @action(methods=["GET"], detail=False, url_path=r"date/(?P<checked_out_date>[^/]+)/list")
    def by_date(self, *args, **kwargs):
        uploaded_date = self.kwargs["checked_out_date"]
        uploaded_date_obj = timezone.datetime.strptime(
            uploaded_date, "%Y-%m-%d")
        contents = UploadedContent.objects.filter(
            checkout_date=uploaded_date_obj)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)


class CheckedContentViewSet(viewsets.ModelViewSet):
    serializer_class = CheckedContentSerializer
    queryset = CheckedContent.objects.all()

    @action(methods=["GET"], detail=False, url_path=r"hospital/(?P<hospital_id>[^/]+)/list")
    def by_hospital(self, *args, **kwargs):
        checked_contents_hospital = self.kwargs["hospital_id"]
        contents = CheckedContent.objects.filter(
            hospital__id=checked_contents_hospital)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)

    @action(methods=["GET"], detail=False, url_path=r"user/(?P<user_id>[^/]+)/list")
    def by_user(self, *args, **kwargs):
        checked_contents_user = self.kwargs["user_id"]
        contents = CheckedContent.objects.filter(
            users__id=checked_contents_user)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)

    @action(methods=["GET"], detail=False, url_path=r"date/(?P<checked_out_date>[^/]+)/list")
    def by_date(self, *args, **kwargs):
        checked_out_date = self.kwargs["checked_out_date"]
        checked_out_date_obj = timezone.datetime.strptime(
            checked_out_date, "%Y-%m-%d")
        contents = CheckedContent.objects.filter(
            checkout_date=checked_out_date_obj)
        serializer_obj = self.serializer_class(contents, many=True)
        return response.Response(serializer_obj.data, status=200)
