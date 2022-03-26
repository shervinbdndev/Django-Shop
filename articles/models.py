from django.db import models
from jalali_date import (date2jalali , datetime2jalali)
from accounts.models import User




class ArticleCategory(models.Model):
    parent = models.ForeignKey(to='ArticleCategory' , null=True , blank=True , on_delete=models.CASCADE , verbose_name='Parent Category')
    title = models.CharField(max_length=200 , verbose_name='Title')
    url_title = models.CharField(max_length=200 , unique=True , verbose_name='URL Title')
    is_active = models.BooleanField(default=True , verbose_name='Active / Inactive')
    
    def __str__(self) -> str:
        super(ArticleCategory , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'
        
        
        
        

class Article(models.Model):
    title = models.CharField(max_length=300 , verbose_name='Title')
    slug = models.SlugField(max_length=400 , db_index=True , allow_unicode=True , verbose_name='URL Title')
    image = models.ImageField(upload_to='images/articles' , verbose_name='Article Image')
    short_description = models.TextField(verbose_name='Short Description')
    text = models.TextField(verbose_name='Text')
    is_active = models.BooleanField(verbose_name='Active / Inactive' , default=True)
    selected_categories = models.ManyToManyField(to=ArticleCategory , verbose_name='Categories')
    author = models.ForeignKey(to=User , on_delete=models.CASCADE , verbose_name='Author' , null=True , editable=False)
    created_at = models.DateTimeField(auto_now_add=True , editable=False , verbose_name='Created At')
    
    def __str__(self) -> str:
        super(Article , self).__str__()
        return self.title
    
    def get_jalali_create_date(self):
        return date2jalali(g_date=self.created_at)
    
    def get_jalali_create_time(self):
        return datetime2jalali(g_date=self.created_at.strftime(format='%H:%M'))
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'