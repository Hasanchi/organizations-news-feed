from django.urls import path

from . import views

from .views import EditPost, CreatePost, ListPost

urlpatterns = [
    path('<slug:division>/', ListPost.as_view(), name='post_list'),
    # path('<slug:slug>/', views.post_list, name='post_list_filter'),
    path('create/', CreatePost.as_view(), name='create'),

]
