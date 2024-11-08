from django.urls import path
from core import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/home/', views.HomeCategoryList.as_view(),
         name='home-category-list'),

    path('', views.ProductList.as_view(), name='product-list'),
    path('popular/', views.PopularProductList.as_view(), name='popular-list'),
    path('bytype/', views.ProductListByClothesType.as_view(), name='list-by-type'),

    path('search/', views.SearchProductByTitle.as_view(), name='search'),
    path('category/', views.FilterProductByCategory.as_view(),
         name='product-by-category'),
    path('recomendations/', views.SimilarProducts.as_view(), name='similar-products')

]
