from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.db.models import Count
import random


class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializers
    queryset = models.Category.objects.all()


class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializers

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:5]


class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializers
    queryset = models.Brand.objects.all()


class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializers

    def get_queryset(self):
        queryset = models.Product.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]


class PopularProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializers

    def get_queryset(self):
        queryset = models.Product.objects.filter(
            ratings__gte=4.0, ratings__lte=5.0)
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]


class ProductListByClothesType(APIView):
    serializer_class = serializers.ProductSerializers

    def get_queryset(self, request):
        query = request.query_params.get('clothesType', None)
        if query:
            queryset = models.Product.objects.filter(clothesType=query)
            queryset = queryset.annotate(random_order=Count('id'))
            products_list = list(queryset)
            random.shuffle(products_list)

            limited_products = products_list[:20]
            serializer = serializers.ProductSerializers(
                limited_products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)


class SimilarProducts(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category=query)
            product_list = list(products)
            random.shuffle(product_list)
            limited_products = product_list[:6]
            serializer = serializers.ProductSerializers(
                limited_products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)


class SearchProductByTitle(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            prosucts = models.Product.objects.filter(title_icontains=query)
            serializer = serializers.ProductSerializers(prosucts, many=True)
            return Response(serializer)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)


class FilterProductByCategory(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)
        if query:
            prosucts = models.Product.objects.filter(category=query)
            serializer = serializers.ProductSerializers(prosucts, many=True)
            return Response(serializer)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)