from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from hospitals.models import Hospital


@pytest.fixture
def new_hospital(db):
    hospital = Hospital.objects.create(
        name='Providence MOB',
        location='350 30th St, Oakland CA 94609',
    )
    return hospital


def test_search_hospitals(new_hospital):
    assert Hospital.objects.filter(name='Providence MOB').exists()
    assert Hospital.objects.filter(
        location='350 30th St, Oakland CA 94609').exists()


def test_update_hospitals(new_hospital):
    new_hospital.name = 'Peralta MOB'
    new_hospital.location = '3100 Telegraph Ave, Oakland CA 94609'
    new_hospital.save()

    assert Hospital.objects.filter(name='Peralta MOB').exists()
    assert Hospital.objects.filter(
        location='3100 Telegraph Ave, Oakland CA 94609').exists()


@pytest.fixture
def client():
    return APIClient()


def test_hospitalList_api(db, client):
    response = client.get(path="/api/hospitals/")
    assert response.status_code == 200


def test_cost_centerList_api(db, client):
    response = client.get(path="/api/cost-centers/")
    assert response.status_code == 200


def test_departmentList_api(db, client):
    response = client.get(path="/api/departments/")
    assert response.status_code == 200
