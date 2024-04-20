from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth import login as auth_login,logout

# Create your views here.

#sign_up page 

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
           d={"msg":"email is already exists"}
           return render(request,'register.html',d)
        else:   
            obj = User.objects.create_user(username = user_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)
            obj.save()
            d = {"msg":"CONGRATS!!REGISTER SUCCESSFULLY !!"}
            return render(request, 'register.html',d)
        
        return  redirect("/")
    else:
        return render(request, 'register.html')




# Create your views here.
def home(request):
    return render(request,"home.html")


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user = authenticate(request, username = user_name, password = pass_word)
        if user is not None:
            auth_login(request,user)
            return render(request,"home.html")
        else:
            d = {"msg":"INVALID USER NAME AND PASSWORD !!"}
            return render(request, 'login.html',d)

    return render(request,"login.html")

def navbar(request):
    return render(request,"deshboard.html") 

def logout_user(request):
    logout(request)
    return redirect("/")  

def change_password(request):
    if request.method=='POST':
       newpass=request.POST.get('newpassword')
       u=User.objects.get(username=request.user.username)
       u.set_password(newpass)
       d={"msg":"password change successfully"}
       return redirect("/",d)
    return render(request,"change_password.html")                 

def crud(request):
    return render(request,"crud.html")

def password_reset(request):
    return render(request,"password_reset.html")    

 
