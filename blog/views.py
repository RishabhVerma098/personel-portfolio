from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.


def allblogs(request):
    blogs = blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def details(request,Blog_ID):
    blogs = get_object_or_404(blog,pk = Blog_ID)
    return render(request,'blog/detailblog.html',{'blogs':blogs})
    

