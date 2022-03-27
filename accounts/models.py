from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile' , verbose_name='Profile Picture' , null=True , blank=True)
    email_active_code = models.CharField(max_length=100 , verbose_name='Email Activation Code')
    about_user = models.TextField(null=True , blank=True , verbose_name='About User')

    def __str__(self) -> str:
        super(User , self).__str__()
        if (self.first_name is not '' and self.last_name is not ''):  
            return self.get_full_name()
        else:
            return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'