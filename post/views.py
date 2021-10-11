from django.shortcuts import render,redirect

from .forms import PostForm
from .models import Post
from dsuser.models import Dsuser
from tag.models import Tag

from django.http import Http404 
from django.core.paginator import Paginator 

# Create your views here.


def post_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            dsuser=Dsuser.objects.get(pk=user_id)

            tags=form.cleaned_data['tags'].split(',')

            post=Post()
            post.title=form.cleaned_data['title']
            post.contents=form.cleaned_data['contents']
            post.img_url=form.cleaned_data['img_url']
            post.userid=dsuser
            post.save()

            for tag in tags:
                if not tag:
                    continue 
                
                _tag,_=Tag.objects.get_or_create(name=tag)
                post.tags.add(_tag)

            #return redirect('/post/list/')

    else:
        form=PostForm()

    return render(request,'post_write.html',{'form':form})

    

