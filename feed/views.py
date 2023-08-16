from typing import Any
from django import http
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Post

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = 'feed/home.html'
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = 'feed/detail.html'
    model = Post
    context_object_name = "post"

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
