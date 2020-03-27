from django.shortcuts import render
from point.views import throw_point

def main(request):
    if request.user.is_active:
        mypoint = throw_point(request)
        return render(request, 'main/main.html', {'mypoint': mypoint})

    return render(request, 'main/main.html')

def table(request):
    if request.user.is_active:
        mypoint = throw_point(request)
        return render(request, 'main/table1.html', {'mypoint': mypoint})

    return render(request, 'main/table1.html')