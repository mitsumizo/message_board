from django.shortcuts import render
from django.utils import timezone
from .models import Data
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

import time
import socket



# Create your views here.
def post_list(request):
    datas = Data.objects.filter(time__lte=timezone.now()).order_by('-time')
    for data in datas:
        data.person_id = data.hash_ipaddress()
    # datas = Data.objects.filter(name__lte='eiji').order_by('-time')
    return render(request, 'blog/post_list.html', {'datas': datas})

def post_detail(request, pk):
    data = get_object_or_404(Data, pk=pk)

    return render(request, 'blog/post_detail.html', {'data': data})


def post_new(request):

    if request.method == "POST":
        time_st = time.time()
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.time = timezone.now()
            datas = Data.objects.filter(name=data.name).order_by('-time')
            if (data.time - datas[0].time).seconds < 15:
                return redirect('error_page')

            host = socket.gethostname()
            data.ipaddress = socket.gethostbyname(host)
            data.save()
            return redirect('post_detail', pk=data.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_person(request, target_name):
    # target_name = target_name.replace(" ", "")
    datas = Data.objects.filter(name=target_name).order_by('-time')
    for data in datas:
        print(data.name)
    return render(request, 'blog/post_person.html', {'datas': datas})

def error_page(request):
    return render(request, 'blog/error_page.html', {})
