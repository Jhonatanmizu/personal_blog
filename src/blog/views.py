from django.shortcuts import HttpResponse, render


def index(request):
    print('index')
    # return HttpResponse('Hello, world. You are at the blog index.')
    return render(request, 'blog/pages/index.html')
