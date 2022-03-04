from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest
from site_settings.models import (SiteSettings , FooterLinkBox , Slider)



class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView , self).get_context_data(**kwargs)
        sliders : Slider = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        return context




class AboutView(TemplateView):
    template_name = 'home/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
        context['setting'] = setting
        return context




def header_component(request : HttpRequest):
    setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
    return render(request=request , template_name='home/header-component.html' , context={'setting':setting})


def footer_component(request : HttpRequest):
    footer_link_box : FooterLinkBox = FooterLinkBox.objects.all()
    setting : SiteSettings = SiteSettings.objects.filter(is_main_setting = True).first()
    for item in footer_link_box:
        item.footerlink_set
    return render(request=request , template_name='home/footer-component.html' , context={'setting':setting,'footer_link_boxes':footer_link_box})