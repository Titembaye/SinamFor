from django.shortcuts import render

# Create your views here.
def blod_list(request):
    return render(request,'blog/blog_list.html')


def blod_detail(request):
    return render(request,'blog/blog_list.html')
