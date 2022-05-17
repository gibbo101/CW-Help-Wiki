from django.shortcuts import render
from django.views import generic
from .models import Category

class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('id')
    template_name = 'index.html'
