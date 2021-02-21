import datetime

from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.
class IndexPage(View):
    model = Post
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        views_sorted_posts = self.model.objects.order_by("-views")
        week_most_views = views_sorted_posts.filter(
            date_published__gt=datetime.date.today() - datetime.timedelta(days=7))
        date_sorted_posts = self.model.objects.order_by("-date_published")
        context["last_news_carousel"] = date_sorted_posts[:12]
        context["four_most_views"] = week_most_views[:4]
        context["last_post"] = date_sorted_posts[0]
        return render(request, self.template_name, context)
