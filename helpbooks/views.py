from django.shortcuts import render
from django.views import generic
from .models import Category, Subject

class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('id')
    template_name = 'index.html'

class SubjectList(generic.ListView):
    model = Subject
    queryset = Subject.objects.order_by('id')
    template_name = 'index.html'
