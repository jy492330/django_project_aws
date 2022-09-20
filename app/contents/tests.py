from django.test import TestCase
from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from contents.models import HostedContent
from contents.models import UploadedContent
from contents.models import CheckedContent
from hospitals.models import Hospital
from users.models import User
import datetime


@pytest.fixture
def new_hospital(db):
    return Hospital.objects.create(name="Providence", location="3100 Summit Street, Oakland CA")


@pytest.fixture
def update_hospital(db):
    return Hospital.objects.create(name="Alta Bates", location="2450 Ashby Ave, Berkeley CA")


@pytest.fixture
def new_user(db):
    return User.objects.create_user(username="Kelly2022", password="12345abcde")


@pytest.fixture
def new_user2(db):
    return User.objects.create_user(username="Joe2022", password="12345abcde")


@pytest.fixture
def update_user(db):
    return User.objects.create_user(username="Jessica2022", password="12345abcde")


@pytest.fixture
def new_hosted_content(db, new_hospital):
    hosted_content = HostedContent.objects.create(
        title='Item South Pavilion_PreOpClinic-CO-02',
        folder_path='/ ABSMC Campuses / Summit Campus / South Pavilion / As-Builts / PDF',
        release_date=datetime.datetime(2022, 9, 1),
        revision=1,
        content_type='Drawings',
        content_subtype='As-Built',
        content_format='PDF',
        hospital=new_hospital,
    )
    return hosted_content


def test_search_hosted_contents(new_hosted_content, new_hospital):
    assert HostedContent.objects.filter(
        title='Item South Pavilion_PreOpClinic-CO-02').exists()
    assert HostedContent.objects.filter(content_type='Drawings').exists()
    assert HostedContent.objects.filter(hospital=new_hospital)


def test_update_hosted_contents(new_hosted_content, update_hospital):
    new_hosted_content.title = 'Item South Pavilion_PreOpClinic-CO-02 Approved_Elec'
    new_hosted_content.content_format = 'DWG'
    new_hosted_content.release_date = datetime.datetime.now().date()
    new_hosted_content.revision = 2
    new_hosted_content.hospital = update_hospital
    new_hosted_content.save()

    assert HostedContent.objects.filter(
        title='Item South Pavilion_PreOpClinic-CO-02 Approved_Elec').exists()
    assert HostedContent.objects.filter(content_format='DWG').exists()
    assert HostedContent.objects.filter(
        release_date=datetime.datetime.now().date()).exists()
    assert HostedContent.objects.filter(revision=2).exists()
    assert HostedContent.objects.filter(hospital=update_hospital).exists()


@pytest.fixture
def new_uploaded_content(db, new_hospital, new_user):
    uploaded_content = UploadedContent.objects.create(
        title='Revit Data Migration_Ashby Occupancy',
        folder_path='/ ABSMC Campuses / Alta Bates Campus / Occupancy Plans / Revit Data Migration',
        upload_date=datetime.datetime(2022, 9, 1),
        hospital=new_hospital,
        user=new_user,
    )
    return uploaded_content


def test_search_uploaded_contents(new_uploaded_content, new_hospital, new_user):
    assert UploadedContent.objects.filter(
        title='Revit Data Migration_Ashby Occupancy').exists()
    assert UploadedContent.objects.filter(
        folder_path='/ ABSMC Campuses / Alta Bates Campus / Occupancy Plans / Revit Data Migration').exists()
    assert UploadedContent.objects.filter(hospital=new_hospital).exists()
    assert UploadedContent.objects.filter(user=new_user).exists()


def test_update_uploaded_contents(new_uploaded_content, update_hospital, update_user):
    new_uploaded_content.title = 'Revit Data Migration_Peralta Occupancy'
    new_uploaded_content.folder_path = '/ ABSMC Campuses / Peralta Campus / Occupancy Plans / Revit Data Migration'
    new_uploaded_content.upload_date = datetime.datetime.now().date()
    new_uploaded_content.hospital = update_hospital
    new_uploaded_content.user = update_user
    new_uploaded_content.save()

    assert UploadedContent.objects.filter(
        title='Revit Data Migration_Peralta Occupancy').exists()
    assert UploadedContent.objects.filter(
        folder_path='/ ABSMC Campuses / Peralta Campus / Occupancy Plans / Revit Data Migration').exists()
    assert UploadedContent.objects.filter(
        upload_date=datetime.datetime.now().date()).exists()
    assert UploadedContent.objects.filter(hospital=update_hospital).exists()
    assert UploadedContent.objects.filter(user=update_user).exists()


@pytest.fixture
def new_checked_content(db, new_hospital, new_user, new_user2):
    checked_content = CheckedContent.objects.create(
        title='Peralta Tomography Architectural Apr-15-2008',
        folder_path='/ ABSMC Campuses / Summit Campus / Peralta / As-Builts / CAD',
        checkout_date=datetime.datetime(2022, 9, 1),
        hospital=new_hospital,
    )
    checked_content.users.set([new_user, new_user2])
    return checked_content


def test_search_checked_contents(new_checked_content, new_hospital, new_user, new_user2):
    assert CheckedContent.objects.filter(
        title='Peralta Tomography Architectural Apr-15-2008').exists()
    assert CheckedContent.objects.filter(
        folder_path='/ ABSMC Campuses / Summit Campus / Peralta / As-Builts / CAD').exists()
    assert CheckedContent.objects.filter(hospital=new_hospital).exists()
    assert new_user in new_checked_content.users.all()
    assert new_user2 in new_checked_content.users.all()


def test_update_checked_contents(new_checked_content, update_hospital, update_user, new_user, new_user2):
    new_checked_content.title = 'Peralta Tomography Architectural Sep-1-2022'
    new_checked_content.folder_path = '/ ABSMC Campuses / Summit Campus / Peralta / As-Builts / PDF'
    new_checked_content.checkout_date = datetime.datetime.now().date()
    new_checked_content.hospital = update_hospital
    new_checked_content.users.add(update_user)
    new_checked_content.save()

    assert CheckedContent.objects.filter(
        title='Peralta Tomography Architectural Sep-1-2022').exists()
    assert CheckedContent.objects.filter(
        folder_path='/ ABSMC Campuses / Summit Campus / Peralta / As-Builts / PDF').exists()
    assert CheckedContent.objects.filter(
        checkout_date=datetime.datetime.now().date()).exists()
    assert CheckedContent.objects.filter(hospital=update_hospital).exists()
    assert new_user in new_checked_content.users.all()
    assert new_user2 in new_checked_content.users.all()
    assert update_user in new_checked_content.users.all()
