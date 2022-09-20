from django.test import TestCase
from django.urls import reverse
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def test_user(db, django_user_model):  
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"  


def test_login_user(client, test_user):
    test_username, test_password = test_user  
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True


@pytest.fixture
def client():
    return APIClient()


def test_userList_api(db, client):
    response = client.get(path="/api/users/")
    assert response.status_code == 200
