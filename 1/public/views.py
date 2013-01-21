# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Home view
    """

    template_name = 'public_home.html'