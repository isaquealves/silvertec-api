"""Conftest plugin module
This module allow sharing some data between tests
"""
import pytest
from orders.models import User
from rest_framework.test import APIClient

@pytest.fixture
def user_ref(transactional_db):
    """ User fixture
    Simple fixture to return a user reference to be used on

    Args:
        transactional_db (fixture): Pytest builtin fixture to
        provide access to db
    """
    user = User.objects.create(username='john',
                               email='johndoe@example.com',
                               password='123')
    return user

@pytest.fixture
def admin_ref(transactional_db):
    return User.objects.create_superuser(
        first_name='First',
        last_name='Last',
        username='admin',
        email='admin@example.com',
        password='12345'
    )

@pytest.fixture
def api_client():
    return APIClient()




