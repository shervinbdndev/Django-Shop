from typing import (Any , Dict)
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http.request import HttpRequest
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
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if (category_name is not None):
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query
    
    
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/articles-details.html'
    
    def get_queryset(self):
        query = super(ArticleDetailView , self).get_queryset()
        query = query.filter(is_active=True)
        return query

    
    


class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/header-component.html' , context={})




class FooterComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/footer-component.html' , context={})
    
    
    

class ArticleCategoriesComponent(View):
    def get(self , request : HttpRequest):
        article_main_categories : ArticleCategory = ArticleCategory.objects.filter(is_active=True , parent_id=None)
        return render(request=request , template_name='articles/articles-cat-comp.html' , context={'main_categories':article_main_categories})