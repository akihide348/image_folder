from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


# class deleteTodo(request, todo_id):
# 	item_to_delete = Post.objects.get(id=todo_id)
# 	item_to_delete.delete()
# 	reverse_lazy('home')