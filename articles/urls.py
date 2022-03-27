from django.urls import path
from . import views



urlpatterns = [
    path(route='' , view=views.ArticlesListView.as_view() , name='articles_page') ,
    path(route='cat/<str:category>' , view=views.ArticlesListView.as_view() , name='articles_by_category_list') ,
    path(route='<pk>/' , view=views.ArticleDetailView.as_view() , name='articles_detail') ,
]