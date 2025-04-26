from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def starting_page(req):
    latest_posts = Post.objects.all().order_by("-date")[:3] # perchè le prime 3? Perchè sto sortando in descending order,that's why eheh
    return render(req, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(req):
    all_posts = Post.objects.all().order_by("-date")
    return render(req, "blog/all-posts.html",{
        "all_posts" : all_posts
    })

def post_detail(req, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(req, "blog/post-details.html", {
        "post" : identified_post,
        "tags" : identified_post.tags.all()
    })