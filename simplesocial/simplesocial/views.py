from django.views.generic import TemplateView

# Define Views Here
class HomePage(TemplateView):
    template_name = 'index.html'