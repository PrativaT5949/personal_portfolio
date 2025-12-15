from django.views import generic
from home.models import Homepage


class HomePageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        instance = Homepage.objects.first()
        data["object"] = instance
        return data
