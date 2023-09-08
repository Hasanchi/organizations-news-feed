from django.shortcuts import render


from .models import Post


def post_list(request, slug=None):
    if slug in Post.TypeNews:
        posts = Post.published.all()
    else:
        posts = Post.published.filter(type=slug)

    return render(request, 'feed/posts/feed.html', {'posts': posts})

