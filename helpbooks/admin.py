from django.contrib import admin
from .models import Category, Subject, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Subject)
class SubjectAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'category', 'created_date', 'author')
    search_fields = ['title']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comments)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('subject', 'author', 'created_date', 'content')
    list_filter = ('subject', 'created_date')
    search_fields = ['content']
    summernote_fields = ('content')