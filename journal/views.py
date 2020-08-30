from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Journal


# Create your views here.


class HomePageView(ListView):
  template_name = 'home.html'
  model = Journal
  
class DetailPageView(DetailView):
  template_name = 'post_detail.html'
  model = Journal
  
class CreatePageView(CreateView):
    template_name = 'create.html'
    model = Journal
    fields = '__all__'


class UpdatePageView(UpdateView):
    template_name = 'update.html'
    model = Journal
    fields = ['title', 'body']


class DeletePageView(DetailView):
    template_name = 'delete.html'
    model = Journal
    success_url = reverse_lazy('home')
