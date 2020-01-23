from orders.serializers import OrderSerializer, UserSerializer

def test_order_serializer():
    serializer = OrderSerializer()
    assert set(serializer.data.keys()) == set([ 'user', 'content'])