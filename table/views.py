from django.shortcuts import get_object_or_404, render, redirect
from point.views import throw_point
from .forms import FreeTableForm, NoticeTableForm
from .models import *
from point.views import throw_point




def post_detail(request, pk):
    post = get_object_or_404(FreeTable, pk=pk)
    mypoint = throw_point(request)
    return render(request, 'table/detail.html', {'mypoint': mypoint, 'post': post})




def free_table(request):
    posts = FreeTable.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    mypoint = throw_point(request)
    return render(request, 'table/free_table.html', {'mypoint': mypoint, 'posts': posts})

def photo_table(request):
    mypoint = throw_point(request)
    return render(request, 'table/photo_table.html', {'mypoint': mypoint})





def freeTable_new(request):
    if request.method == "POST":
        form = FreeTableForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = FreeTableForm()

        if request.user.is_active:
            mypoint = throw_point(request)
            return render(request, 'table/writing.html', {
                'mypoint': mypoint,
                'form': form
            })

    return render(request, 'table/writing.html')



def noticeTable_new(request):
    if request.method == "POST":
        form = NoticeTableForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('notice', pk=post.pk)
    else:
        form = NoticeTableForm()

    if request.user.is_active:
        mypoint = throw_point(request)
        return render(request, 'table/writing.html', {
            'mypoint': mypoint,
            'form': form
        })

    return render(request, 'table/writing.html')
