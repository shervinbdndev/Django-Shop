from typing import (Any , Dict)
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.http.request import HttpRequest
from jalali_date import datetime2jalali
from .models import Article, ArticleCategory




class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'articles/articles.html'
    
    def get_context_data(self, *args , **kwargs: Any) -> Dict[str, Any]:
        context = super(ArticlesListView , self).get_context_data(*args , **kwargs)
        return context
    
    def get_queryset(self):
        query = super(ArticlesListView , self).get_queryset()
        category_name = self.kwargs.get('category')
        if (category_name is not None):
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query
    
    


class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/header-component.html' , context={})




class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/footer-component.html' , context={})
    
    
    

class ArticleCategoriesComponent(View):
    def get(self , request : HttpRequest):
        article_main_categories : ArticleCategory = ArticleCategory.objects.filter(is_active=True , parent_id=None)
        return render(request=request , template_name='articles/articles-cat-comp.html' , context={'main_categories':article_main_categories})