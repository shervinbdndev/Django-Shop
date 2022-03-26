from django.contrib import admin
from django.http.request import HttpRequest
from .models import (ArticleCategory , Article)





class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'url_title' , 'parent' , 'is_active']
    list_editable = ['url_title' , 'parent' , 'is_active']
    
    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug' , 'is_active' , 'author']
    list_editable = ['is_active']
    
    def save_model(self, request : HttpRequest, obj : Article, form, change):
        if (not change):
            obj.author = request.user
        return super(ArticleAdmin , self).save_model(request, obj, form, change)
    



admin.site.register(ArticleCategory , ArticleCategoryAdmin)
admin.site.register(Article , ArticleAdmin)