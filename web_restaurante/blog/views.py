from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogTemplateView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'autor', 'published', 'categories', 'image']
    success_url = reverse_lazy('blog:blog')


class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog')


"""def updateBlog(req):
    return render(req, "blog/blog_update_form.html")
"""


class BlogUpdateView(UpdateView):
    print("Entrando a blog update")
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('blog:update', args=[self.object.id])+'?ok'


'''
# Create your views here.
def blog(req):
    posts = Post.objects.all()
    return render(req, "blog/blog.html", {'posts' : posts})
'''


def category(req, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(req, "blog/category.html", {'category': category})
