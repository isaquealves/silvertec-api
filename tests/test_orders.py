import pytest
import json
from orders.models import Order


def test_can_create_order(user_ref):
    data = {
        'data': 'sampledata'
    }
    Order.objects.create(
        user=user_ref,
        content=json.dumps(data)
    )

    assert Order.objects.count() == 1

def test_route_order_list_per_user_exists(api_client, user_ref):

    data = {
        'data': 'sampledata'
    }
    Order.objects.create(
        user=user_ref,
        content=json.dumps(data)
    )

    response = api_client.get(f'/users/{user_ref.id}/orders')
    assert response.status_code == 200


