from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from . import models

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

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #Inherited listview school_list natively.  forced to 'schools'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreate(CreateView):
    model = models.School
    fields = ('name', 'size', 'site')
    template_name = 'basic_app/school_form.html'
    
class SchoolUpdate(UpdateView):
    model = models.School
    fields = ('size', 'site')

class SchoolDelete(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")