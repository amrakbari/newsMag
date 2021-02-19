from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post


# Create your views here.
class IndexPage(ListView):
    queryset = Post.objects.all()
    template_name = "index.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(IndexPage, self).get_context_data(*args, **kwargs)
        context["four_most_views"] = Post.objects.order_by("views")
        print(context)
        return context
