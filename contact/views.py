from django.urls import reverse
from django.shortcuts import (render , redirect)
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http.response import HttpResponse
from site_settings.models import (SiteSettings , FooterLinkBox)
from .forms import ContactUsModelForm
from .models import (ContactUs , UserProfile)




class ContactUsView(View):
    def get(self , request : HttpResponse):
        contact_form = ContactUsModelForm()
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
        return render(request=request , template_name='contact/contact.html' , context={'contact_form':contact_form,'setting':setting})

    def post(self , request : HttpResponse):
        contact_form = ContactUsModelForm(request.POST or None)
        if (contact_form.is_valid()):
            contact_form.save()
            return redirect(to=reverse('home_page'))
        return render(request=request , template_name='contact/contact.html' , context={'contact_form':contact_form})




class CreateProfileView(CreateView):
    template_name = 'contact/create-profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = 'contact-us/create-profile'




class ProfilesView(ListView):
    template_name = 'contact/profiles-list.html'
    model = UserProfile
    context_object_name = 'profiles'




class HeaderComponentView(View):
    def get(self , request : HttpResponse):
        return render(request=request , template_name='contact/header-component.html' , context={})




class FooterComponentView(View):
    def get(self ,request : HttpResponse):
        footer_link_boxes : FooterLinkBox = FooterLinkBox.objects.all()
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
        for item in footer_link_boxes:
            item.footerlink_set
        return render(request=request , template_name='contact/footer-component.html' , context={'setting':setting,'footer_link_boxes':footer_link_boxes})