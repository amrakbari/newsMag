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
        four_most_views = self.model.objects.filter(date_published__gt=datetime.date.today() -
                                                                       datetime.timedelta(days=7)).order_by("views")[:4]
        date_ordered_posts = self.model.objects.order_by("date_published")
        last_post = date_ordered_posts[:1]
        context["four_most_views"] = four_most_views
        return render(request, self.template_name, context)
