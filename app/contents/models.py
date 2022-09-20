from operator import mod
from django.db import models



class HostedContent(models.Model):
    CONTENT_TYPES = [
        ['Reports', 'Reports'],    
        ['Drawings', 'Drawings'],
        ['Specs', 'Specs'],
        ['Other', 'Other'],
    ]

    CONTENT_SUBTYPES = [
        ['Base Plan', 'Base Plan'],
        ['As-Built', 'As-Built'],
        ['Occupancy Plan', 'Occupancy Plan'],
        ['Vacancy Plan', 'Vacancy Plan'],
        ['Smoke Compartment', 'Smoke Compartment'],
        ['Life Safety', 'Life Safety'],
        ['Air Relationship', 'Air Relationship'],
        ['Contract and Leasing Exhibits', 'Contract and Leasing Exhibits'],
        ['Maps and Signage', 'Maps and Signage'],
        ['Other', 'Other'],
    ]

    title = models.CharField(max_length=100, unique=True, null=False)
    folder_path = models.CharField(
        max_length=300, unique=False, null=False, blank=False)
    release_date = models.DateField(unique=False, null=True, blank=False)
    revision = models.IntegerField(unique=False, null=True, blank=False)
    content_type = models.CharField(
        max_length=20, choices=CONTENT_TYPES, unique=False, null=True, blank=False)
    content_subtype = models.CharField(
        max_length=50, choices=CONTENT_SUBTYPES, unique=False, null=True, blank=True)
    content_format = models.TextField(unique=False, null=True, blank=True)

    hospital = models.ForeignKey(
        'hospitals.Hospital', related_name="hosted_contents", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UploadedContent(models.Model):
    title = models.CharField(max_length=100, unique=False, null=False)
    upload_date = models.DateField(unique=False, null=False)
    folder_path = models.CharField(max_length=200, unique=False, null=False)

    hospital = models.ForeignKey(
        'hospitals.Hospital', related_name="uploaded_contents", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', related_name="uploaded_contents", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class CheckedContent(models.Model):
    title = models.CharField(max_length=100, unique=False, null=False)
    checkout_date = models.DateField(unique=False, null=False)
    folder_path = models.CharField(max_length=200, unique=False, null=False)
    
    hospital = models.ForeignKey(
        'hospitals.Hospital', related_name="checked_contents", on_delete=models.CASCADE)
    
    users = models.ManyToManyField(
        'users.User', related_name="checked_contents")

    def __str__(self):
        return self.title
