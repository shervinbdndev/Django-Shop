from django.shortcuts import redirect, render
from django.http import Http404
from django.views import View
from django.http import HttpRequest
from django.views.generic.list import ListView
from .models import Product




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
    




def product_detail(request : HttpRequest , pk):
    try:
        product_details = Product.objects.get(id=pk)
    except:
        raise Http404()
    return render(request=request , template_name='product/product-detail.html' , context={'product_details':product_details})




def header_component(request : HttpRequest):
    return render(request=request , template_name='product/header-component.html' , context={})