from django.shortcuts import render
from point.views import throw_point

def main(request):
    mypoint = throw_point(request)
    return render(request, 'main/main.html', {'mypoint': mypoint})

def free_table(request):
    mypoint = throw_point(request)
    return render(request, 'main/free_table.html', {'mypoint': mypoint})
