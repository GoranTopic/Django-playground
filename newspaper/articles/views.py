from django.shortcuts import render
from django.contrib.auth.mixins import  ( LoginRequiredMixin, UserPassesTestMixin )
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy 
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(ListView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView( UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    # Set the logged inuser to be the author of the new article
    def form_vaild(self, form):
        form.instance.autho = self.request.user 
        return super().form_valid(form)




