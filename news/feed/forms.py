from django.forms import ModelForm

from .models import Post


class EditPost(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'status')


class CreatePost(ModelForm):

    class Meta:
        model = Post
        fields = ('__all__')
