from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Post, Category
from django.views.generic.base import TemplateView


class BlogPageView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


'''
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})
'''


def category(request, category_id):
    #category = get_object_or_404(Category, id=category_id)
    category = Category.objects.get(id=category_id)
    #posts = category.post_set.all()
    #posts = Post.objects.filter(categories=category)
    # return render(request, 'blog/category.html', {'category': category, 'posts': posts})
    return render(request, 'blog/category.html', {'category': category})
