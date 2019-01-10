from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.

#Function-based view
# def index(request):
#     return render(request, 'index.html')

#Class-based view
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based Views are COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected_content'] = 'Basic Injection!'
        return context
