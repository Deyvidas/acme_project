from django.views.generic import TemplateView

from birthday.models import Birthday


class HomePage(TemplateView):
    """This view class used for work with static templates without connection with DB."""

    template_name = 'pages/index.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data['total_count'] = Birthday.objects.count()
        return response
