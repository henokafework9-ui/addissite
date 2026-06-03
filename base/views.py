from django.shortcuts import render , redirect
from .models import Blogs
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


# Create your views here.

def register(request): 
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            
            user = form.save()
            
            login(request,user)
            
            return redirect('home/')
    
    return render(request , 'register.html' , {'form':form})    
        

def login_view(request):

    form =AuthenticationForm()

    if request.method =='POST':


        form = AuthenticationForm(request ,data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')

            user = authenticate(request ,username=username,password=password )
            if user is not None:
                login(request,user)
                return redirect('home')
            

    return render(request,'login.html',{'form':form})

def home(request):
    blogs = Blogs.objects.all().order_by('-cratedat')

    return render(request , 'home.html' ,{'blogs':blogs})


    

