from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from wishlist import models, serializers


class GetWishlist(generics.ListAPIView):
    serializer_class = serializers.WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Wishlist.objects.filter(userId=self.request.user)


class ToggleWishlist(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.id
        product_id = request.query_params.get("id")

        if not user_id or not product_id:
            return Response(
                {"message": "Invalid request a user id and product id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            product = models.Product.objects.get(id=product_id)
        except models.Product.DoesNotExist:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        wishlist_item, created = models.Wishlist.objects.get_or_create(
            userId=request.user, product=product
        )
        if created:
            return Response(
                {"message": "Product added to wishlist"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Product removed from wishlist"},
                status=status.HTTP_204_NO_CONTENT,
            )
