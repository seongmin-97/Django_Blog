from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

# Create your views here.

class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(detailView) :
    model = Post

class PostAV(ArchiveIndexView) :
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView) :
    model = Postdate_field = 'modify_dt'
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView) :
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_dt'