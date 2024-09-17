from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
import time


def login_success(sender,request,user,**kwargs):
    print("Login was successfull")
    print("sender",sender)
    print("Request",request)
    print("User",sender)
    time.sleep(20)

    


def login_step2(sender,request,user,**kwargs):
    print("Sent notification")


def logout_notify(sender,request,user,**kwargs):
    print("User Logout succesfully",User.objects.all)

user_logged_in.connect(login_success,sender=User)
user_logged_in.connect(login_step2,sender=User)
user_logged_out.connect(logout_notify,sender=User)

class Rectangle:
   def __init__(self,length,width):
        self.length=length
        self.width=width

   def __str__(self):
      return  str({f'length:{self.length},width:{self.width}'})

a=Rectangle(4,5)
b=Rectangle(5,6)
print(a)
print(b)


