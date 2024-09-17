# Technicalquestions
Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic

A)By default  django signals are  executed synchronously a sender can have multiple receiver function sunscribed to it and all receiever function called one at a time in order they have registered.
example code
Here we user django built in model user and built in signals logged_in,logged_out
Here sender is user and receiver function is login_success,login_step2 
login_success executes when user logs in django admin page and after login_step2 is called then login succesfully is printed in  terminal

from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User

from django.dispatch import receiver

import time

#called when user login 


def login_success(sender,request,user,**kwargs):
   
    print("Login was successfull")
    
    print("sender",sender)
    
    print("Request",request)
    
    print("User",sender)

#after this this will be executed

def login_step2(sender,request,user,**kwargs):
    
    print("Sent notification")

user_logged_in.connect(login_success,sender=User)#first we registered login_success it will be executed first
user_logged_in.connect(login_step2,sender=User)#After login_sucess this will be called

As we can see here login_succes and login_step2 dependent on each other hence django signals are executed synchronously

Question 2: Do django  ? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

A)Yes Django signal run in the same thread as caller to aviod multithreading and concurrency issues let take above example and modify to prove it

Here in this example when user log in in django admin page the signal calls login_success function after 20 seconds when function completed successfully then only user will be logged in django admin page till then it keeps loading until login_success  is executed this proves signals run in the same thread as the caller.
import time
#called when user login 
def login_success(sender,request,user,**kwargs):

    print("Login was successfull")
    
    print("sender",sender)
    
    print("Request",request)
    
    print("User",sender)
    
    time.sleep(20)
user_logged_in.connect(login_success,sender=User)

Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

A)Yes django signals run in the same database transaction as the caller to maintain integrity and acid properites and to avoid transcation concurrency problem django uses single thread for signals run  and database transaction as the caller.
Lets  take above example
When user logs his creditionals is checked in database after validation the user login then login_sucess function is called here it is done by single thread database transcation,signal,receiver function execution to aviod failure and to maintain intergrity and acid properites

Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

A)

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
