from django.shortcuts import render
from point.views import throw_point

def free_table(request):
    mypoint = throw_point(request)
    return render(request, 'table/free_table.html', {'mypoint': mypoint})

def write(request):
    if request.user.is_active:
        mypoint = throw_point(request)
        return render(request, 'write/writing.html', {'mypoint': mypoint})

    return render(request, 'write/writing.html')
