from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import BlogPost
# Create your views here.

#blogs - CRUD: create, read, update, delete
def create_blog_post(request):
    form = None
    context = {"form":form}
    return render(request, "posts/create.html", context)

def list_posts_view(request):
    # obj = get_object_or_404(BlogPost)
    obj = BlogPost.objects.filter()
    context = {"object":obj}
    return render(request, "posts/list.html", context)
    # return HttpResponse("<h1>Mpumeleleo </h1>")

def detial_post_view(request, slug): #add the slug argument for the DB lookup
    obj = get_object_or_404( BlogPost, slug = slug )
    # ob = get_object_or_404(BlogPost, slug) 
    print(slug , "-----------------------------------------------------------")
    context = {"object":obj}
    return render(request, "posts/detial.html", context)

def update_post_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    form = None
    context = {"object":obj, "form":form}
    return render(request, "posts/update.html", context)

def delete_post_view(request,slug): #add the slug argument for the DB lookup
    obj = get_object_or_404(BlogPost, slug = slug)
    context = {"object":obj}
    return render(request, "posts/delete.html", context)


def contact_view(request):
    form = None
    context = {"form": form }
    print(request.POST["full_name"])
    return render(request, "contact.html", context)