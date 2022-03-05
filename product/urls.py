from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path(route='' , view=views.ProductListView.as_view() , name='product_list') ,
    path(route='product-favorite' , view=views.AddProductFavorite.as_view() , name='product-favorite') ,
    path(route='<int:pk>' , view=views.ProductDetailView.as_view() , name='product_detail')
]