import datetime

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post


# Create your views here.
class IndexPage(TemplateView):
    template_name = "index.html"
    mostViews = Post.objects.order_by("-views")
    lastPosts = Post.objects.order_by("-date_published")

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context["top_ten_views"] = self.mostViews[:10]
        return context
