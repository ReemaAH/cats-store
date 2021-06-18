from django.shortcuts import render
from .models import Cat

def store_view(request):
    posts = Cat.objects.all()
    
    context = {
    'post_list': posts
    }
    return render(request, "cats_list.html", context)

