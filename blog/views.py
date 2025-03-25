from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



"""
def home(request):
    return render(request,'blog/home.html', {'posts': Post.objects.all()} )         # Post.objects.all() --> [<Post:Blog 1>, <Post:Blog 2>, <Post:Blog 3>]
"""

# home view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'     # by default : <app/model_viewtype.html>
    context_object_name = 'posts'        # by default : object_list
    ordering = ['-date_posted']



class PostDetailView(DetailView):
    model  = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model  = Post
    fields =  ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model  = Post
    fields = ['title','content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):                      # UserPassesTestMixin runs this test_func
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        



class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




# about view    
def about(request):
    return render(request,'blog/about.html',{'title':'about'})          



