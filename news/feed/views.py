from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from .models import Post
from .forms import EditPost, CreatePost


# def post_list(request, slug=None):
#     if slug in Post.TypeNews:
#         posts = Post.published.all()
#     else:
#         posts = Post.published.filter(type=slug)

#     return render(request, 'feed/posts/feed.html', {'posts': posts})


class Filter:
    def get_type(self):
        return Post.TypeNews.labels


class ListPost(ListView, Filter):
    template_name = 'feed/posts/feed.html'
    paginator_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страницы'

        return context


class CreatePost(CreateView):
    form_class = CreatePost
    success_url = reverse_lazy('feed:post_list')
    template_name = 'feed/posts/create.html'


class EditPost(UpdateView):
    model = Post
    template_name = ''
    success_url = reverse_lazy('feed:detail')
    


class ModelNameDeleteView(DeleteView):
    model = Post
    template_name = 'template.html'
    

