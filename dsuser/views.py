from django.shortcuts import render,redirect 
from .models import Dsuser
from django.http import HttpResponse 
from django.contrib.auth.hashers import check_password,make_password 
from .forms import LoginForm
from post.models import Post

from django.http import Http404 
from django.core.paginator import Paginator 



def home(request):   #post list보여줌
   
    all_posts=Post.objects.all().order_by('-register_date')
    #print('xxxx is ',all_posts)
    page=int(request.GET.get('p',1))
    paginator=Paginator(all_posts,4)

    posts=paginator.get_page(page)
    return render(request,'home.html',{'posts':posts})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            request.session['user']=form.userid
            request.session['username']=form.username
            print('xxxxx',form.userid)
            return redirect('/')
    else:
        form=LoginForm()

    return render(request,'login.html',{'form':form})

def logout(request):
    if request.session.get('user'): 
        del(request.session['user']) 
    return redirect('/')
        

def register(request):
    if request.method=='GET': 
        return render(request,'register.html')
    elif request.method=='POST':
       
        userid=request.POST.get('userid',None)
        email=request.POST.get('useremail',None)
        password=request.POST.get('password',None)
        re_password=request.POST.get('re-password',None)

        res_data={}

        if not (userid and password and re_password and email):
            res_data['error']='모든 값을 입력해야 됩니다.😂'
        elif password!=re_password:
            res_data['error']='비밀번호가 다릅니다'
        else:
            dsuser=Dsuser(
                userid=userid,
                useremail=email,
                password=make_password(password)
            )
            dsuser.save()
            return redirect('/')
           
        return render(request,'register.html',res_data)

# Create your views here.


