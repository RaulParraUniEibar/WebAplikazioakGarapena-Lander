from django.shortcuts import render

from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index (request):
    postak = Post.objects.all
    return render(request, 'index.html', {'posta':postak})

def add(request):
    return render(request,'add.html')

def addpost(request):
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    postberria = Post(izenburua=iz, edukia=ed,noizsortua="")
    postberria.save()

    return HttpResponseRedirect(reverse('index'))