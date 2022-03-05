from django.shortcuts import redirect, render
from django.http.response import Http404
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.views.generic.list import ListView
from .models import Product
from site_settings.models import (FooterLinkBox , SiteSettings)




class ProductListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 9




class AddProductFavorite(View):
    def post(self , request : HttpRequest):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorite'] = product_id
        return redirect(to=product.get_absolute_url())
    




class ProductDetailView(View):
    def get(self , request : HttpRequest , pk):
        try:
            product_details = Product.objects.get(id=pk)
        except:
            raise Http404()
        return render(request=request , template_name='product/product-detail.html' , context={'product_details':product_details})




class HeaderComponentView(View):
    def get(self , request : HttpRequest):
        return render(request=request , template_name='accounts/header-component.html' , context={})




class FooterComponentView(View):
    def get(self , request : HttpRequest):
        footer_link_boxes : FooterLinkBox = FooterLinkBox.objects.all()
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
        for item in footer_link_boxes:
            item.footerlink_set
        return render(request=request , template_name='accounts/footer-component.html' , context={'setting':setting,'footer_link_boxes':footer_link_boxes})