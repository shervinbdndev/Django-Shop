from django.shortcuts import (redirect, render)
from django.urls import reverse
from django.views.generic.base import View
from django.http.response import Http404
from django.http.request import HttpRequest
from django.utils.crypto import get_random_string
from django.contrib.auth import (login , logout)
from utils.email_service import send_email
from site_settings.models import (FooterLinkBox , SiteSettings)
from .forms import (RegisterForm , LoginForm , ForgetPasswordForm , ResetPasswordForm)
from .models import User




class RegisterView(View):
    def get(self , request : HttpRequest):
        register_form = RegisterForm()
        return render(request=request , template_name='accounts/register.html' , context={'register_form':register_form})

    def post(self , request : HttpRequest):
        register_form = RegisterForm(request.POST or None)
        if (register_form.is_valid()):
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user : bool = User.objects.filter(email__iexact=user_email).exists()
            if (user):
                register_form.add_error(field='email' , error='ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(
                    email=user_email ,
                    email_active_code=get_random_string(length=85) ,
                    is_active=False ,
                    username=user_email
                )
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری' , new_user.email , {'user':new_user} , 'emails/activate_account.html')
                return redirect(to=reverse('login_page'))
        return render(request=request , template_name='accounts/register.html' , context={'register_form':register_form})





class ActivateAccountView(View):
    def get(self , request : HttpRequest , email_active_code):
        user : User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if (user is not None):
            if (not user.is_active):
                user.is_active = True
                user.email_active_code = get_random_string(length=85)
                user.save()
                return redirect(to=reverse('login_page'))
            else:
                pass
        raise Http404





class LoginView(View):
    def get(self , request : HttpRequest):
        login_form = LoginForm()
        return render(request=request , template_name='accounts/login.html' , context={'login_form':login_form})

    def post(self , request : HttpRequest):
        login_form = LoginForm(request.POST or None)
        if (login_form.is_valid()):
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user : User = User.objects.filter(email__iexact=user_email).first()
            if (user is not None):
                if (not user.is_active):
                    login_form.add_error(field='email' , error='حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(raw_password=user_password)
                    if (is_password_correct):
                        login(request=request , user=user)
                        return redirect(to=reverse('home_page'))
                    else:
                        login_form.add_error(field='email' , error='نام کاربری یا کلمه عبور اشتباه است')
            else:
                login_form.add_error(field='email' , error='کاربری با مشخصات وارد شده یافت نشد')
        return render(request=request , template_name='accounts/login.html' , context={'login_form':login_form})





class ForgetPasswordView(View):
    def get(self , request : HttpRequest):
        forget_password_form = ForgetPasswordForm()
        return render(request=request , template_name='accounts/forgot.html' , context={'forget_password_form':forget_password_form})

    def post(self , request : HttpRequest):
        forget_password_form = ForgetPasswordForm(request.POST or None)
        if (forget_password_form.is_valid()):
            user_email = forget_password_form.cleaned_data.get('email')
            user : User = User.objects.filter(email__iexact=user_email).first()
            if (user is not None):
                send_email('فعالسازی حساب کاربری' , user.email , {'user':user} , 'emails/forget_password.html')
                return redirect(to=reverse('home_page'))
        return render(request=request , template_name='accounts/forgot.html' , context={'forget_password_form':forget_password_form})





class ResetPasswordView(View):
    def get(self , request : HttpRequest , active_code):
        user : User = User.objects.filter(email_active_code__iexact=active_code).first()
        if (user is None):
            return redirect(to=reverse('login_page'))
        reset_password_form = ResetPasswordForm()
        return render(request=request , template_name='accounts/reset.html' , context={'reset_password_form':reset_password_form,'user':user})

    def post(self , request : HttpRequest , active_code):
        reset_password_form = ResetPasswordForm(request.POST or None)
        user : User = User.objects.filter(email_active_code__iexact=active_code).first()
        if (reset_password_form.is_valid()):
            if (user is None):
                return redirect(to=reverse('login_page'))
            user_new_password = reset_password_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(length=85)
            user.is_active = True
            user.save()
            return redirect(to=reverse('login_page'))
        return render(request=request , template_name='accounts/reset.html' , context={'reset_password_form':reset_password_form,'user':user})





class LogoutView(View):
    def get(self , request : HttpRequest):
        logout(request=request)
        return redirect(to=reverse('login_page'))
    
    
    
    

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