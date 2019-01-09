from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

#Function-based view
# def index(request):
#     return render(request, 'index.html')

#Class-based view
class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based Views are COOL!")