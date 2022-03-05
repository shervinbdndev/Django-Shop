from django.shortcuts import render
from django.views.generic.base import View
from django.http.request import HttpRequest
from .models import Article




class ArticlesView(View):
    def get(self , request : HttpRequest):
        articles : Article = Article.objects.filter(is_active=True)
        return render(request=request , template_name='articles/articles.html' , context={'articles':articles})
    
    


class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/header-component.html' , context={})




class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='articles/footer-component.html' , context={})