from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'myapp/post_list.html', {})

def about(request):
    return render(request, 'myapp/about.html', {})

