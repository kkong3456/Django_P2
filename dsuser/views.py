from django.shortcuts import render,redirect 
from .models import Dsuser
from django.http import HttpResponse 
from django.contrib.auth.hashers import check_password,make_password 


def register(request):
    if request.method=='GET':
      
        return render(request,'register.html')
    elif request.method=='POST':
        print('GGGGGGGGGGGGGGGGGGGGGGGGGGGG')
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
        
        return render(request,'register.html',res_data)

# Create your views here.


