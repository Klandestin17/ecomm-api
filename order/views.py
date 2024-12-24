from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from notification.models import Notification
from order import models, serializers
from core.models import Product
from extras.models import Address
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class AddOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, requset):
        data = requset.data

        try:
            with transaction.atomic():
                validated_products = []

                for product_data in data["order_products"]:
                    product = get_object_or_404(Product, id=product_data["product"])

                    validated_products.append(
                        {
                            "product_id": product.id,
                            "imageUrl": product.imageUrl[0],
                            "title": product.title,
                            "price": product_data["quantity"],
                            "size": product_data["size"],
                            "color": product_data["color"],
                        }
                    )

                    address = get_object_or_404(Address, id=int(data["address"]))
                    order = models.Order.objects.create(
                        user=requset.user,
                        customer_id=data["customer_id"],
                        address=address,
                        order_products=validated_products,
                        rated=[0],
                        total_quantity=data["total_quantity"],
                        subtotal=data["subtotal"],
                        total=data["total"],
                        delivery_status=data["delivery_status"],
                        payment_status=data["payment_status"],
                    )

                    title = "Order Successfully Placed"
                    message = "Your payment has ben successfully and your"

                    Notification.objects.create(
                        orderId=order, title=title, message=message, userId=requset.user
                    )

                    order.save()

                    return Response({"id": order.id}, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response(
                {"message": "one or more product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Address.DoesNotExist:
            return Response(
                {"message": "user address not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except KeyError as e:
            return Response(
                {"message": f"Missing key :{str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserOrdersByStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, requset):
        order_status = requset.query_params.get("status")

        user = requset.user
        orders = models.Order.objects.filter(
            user=user, delivery_status=order_status
        ).order_by("-created_at")

        serializer = serializers.OrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_id = request.query_params.get("id")

        order = get_object_or_404(models.Order, id=order_id)
        serializer = serializers.OrdersSerializer(order)

        return Response(serializer.data, status.HTTP_200_OK)
