
from rest_framework import status
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from orders.models import Order, User
from orders.serializers import OrderSerializer

def orders_list(request, userid, format=None):
    if request.method == 'GET':
        orders = Order.objects.filter(user__pk=userid)
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
