from django.http import JsonResponse
from psycopg2.extensions import JSONB
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from  rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from ..models import Product, PartnerTask
from ..serializers.serializers import (
    ProductSerializer,
    PartnerTaskSerializer
)



@api_view(['POST'])
def products(request: Request) -> Response:
    products = ProductSerializer(Product.objects.all(), many=True)

    return Response(
        data=products.data,
        status=status.HTTP_200_OK
    )
@api_view(['GET'])
def get_product(request, id) -> Response:
    try:
        product = Product.objects.get(id=id)
        return Response(
            data=ProductSerializer(product).data,
            status=status.HTTP_200_OK
        )
    except ObjectDoesNotExist as e:
        return Response(
            data={}
        )
@api_view(['POST'])
def create_product(request: Request) -> Response:
    product: dict = request.data.get('product')
    serializer_data = ProductSerializer(data=product)
    if serializer_data.is_valid():
        data = serializer_data.data
        new_product = Product(
            name=data.get('name'),
            price=data.get('price'),
            stock=data.get('stock'),
            category_id=1)
        new_product.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tasks(request: Request) -> Response:
    try:
        tasks: list[dict] = PartnerTaskSerializer(PartnerTask.objects.all(), many=True).data
        print(tasks)
        return Response(
            data=tasks,
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            data=tasks,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
