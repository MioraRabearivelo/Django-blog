from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView # ListView permet de recuperé toutes les données dans notre model
from  posts.models import BlogPost

# Create your views here.

class BlogHome(ListView):
    model = BlogPost # le model que nous utilisons
    context_object_name = "posts" # Qui nous permet de specifier les variable dans notre templates

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    """
        cette classe permet de remplir une formulaire
    """
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content', ] # ce que nous voulons afficher dans le templates


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"


class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")