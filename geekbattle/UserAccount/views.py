import random
import hashlib
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import UserModel
from level_1.models import Answer

def is_username_exist(username):
    if User.objects.filter(username=username).count():
        return True
    return False
 
def signup(request):
    if request.method == "GET":
        return render(request,'UserAccount/register.html')
    elif request.method == "POST":
        if not(is_username_exist(request.POST.get('username'))):
	    activation_key = str(random.randint(10000,99999))
            obj=UserModel(model_username=request.POST.get('username',''),model_password=request.POST.get('password',''),model_activation_key=activation_key)
	    obj.save()
	    send_mail('Verificationmail','Please use this link to activate your account:http://geekbattle.asetalias.in/user/activate/%s'% activation_key,'kushagra343@gmail.com',[request.POST.get('username','')],fail_silently=False)		
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return HttpResponseRedirect(reverse('user:signup'))
 

def signup1(request):
 if request.method =='POST':
     if not(is_username_exist(request.POST.get('username'))):
	 activation_key = str(random.randint(10000,99999))
         #send_mail('Verificationmail','Please use this link to activate your account:http://geekbattle.asetalias.in/user/activate/%s'% activation_key,'kushagra343@gmail.com',[request.POST.get('username','')],fail_silently=False)
         #encoded_string = hashlib.md5(request.POST.get('password','')).hexdigest()
	 obj=UserModel(model_username=request.POST.get('username',''),model_password=request.POST.get('password',''),model_activation_key=activation_key)
	 obj.save()      	
      	 return HttpResponseRedirect(reverse('user:login'))        
 return render(request,'UserAccount/register.html')


def activate(request,offset):
  if UserModel.objects.filter(model_activation_key=offset).count()==0:
	return HttpResponseRedirect(reverse('level_1:home'))
  obj=UserModel.objects.get(model_activation_key=offset)	
  if User.objects.filter(username=obj.model_username).count()==0:
    user = User.objects.create_user(username = obj.model_username, password = obj.model_password)
    user.save()
    answer_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    active_status_list = answer_list	
    Answer.objects.create(user=User.objects.get(username=obj.model_username), answer_list=answer_list,active_status_list=active_status_list)	
  return HttpResponseRedirect(reverse('user:login'))



def login(request):
    if request.user.is_authenticated():
     return HttpResponseRedirect(reverse('level_1:home')) 
    elif request.method == "GET":
        return render(request,'UserAccount/login.html')
    elif request.method=="POST":
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('level_1:home'))
        else:
            messages.add_message(request, messages.INFO, 'Username or Password is incorrect')
            return HttpResponseRedirect(reverse('user:login'))

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(reverse('user:login'))



def forget_password(request):
 if request.method=='POST': 
  user_name = request.POST.get('username', False)
  if User.objects.filter(username=user_name).count():
    obj=UserModel.objects.get(model_username=user_name)
    obj.model_activation_key=obj.model_activation_key+12345 
    obj.save()			
    send_mail('Password Reset Link','Please use this link to reset your password:http://geekbattle.asetalias.in/password_forget/%s'% obj.model_activation_key,'kushagra343@gmail.com',[user_name],fail_silently=False)
    return render(request,'UserAccount/forget_success.html') 
  else:
   return render(request,'UserAccount/password_forget1.html')
 else: 
  return render(request,'UserAccount/password_forget.html') 

def password_reset(request,offset):
 if request.method=='POST': 
  obj=UserModel.objects.get(model_activation_key=offset)
  user = User.objects.get(username=obj.model_username)
  if request.POST.get('password1', False)!=request.POST.get('password2', False): 
   return render(request,'password_reset1.html')
  user.set_password(request.POST.get('password1',''))
  user.save()
  return HttpResponseRedirect(reverse('user:login'))
 else:
  return render(request,'UserAccount/password_reset.html')

