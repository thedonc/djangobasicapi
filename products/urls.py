from django.urls import path
from .views import product_list, product_detail #ProductDeailView, ProductListView

'''
urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDeailView.as_view(), name="product-detail")
]
'''
urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail")
]
