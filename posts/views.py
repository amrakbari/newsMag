from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.
class IndexPage(View):
    model = Post
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        four_most_views = self.model.objects.order_by("views")[:4]
        context["four_most_views"] = four_most_views
        return render(request, self.template_name, context)
