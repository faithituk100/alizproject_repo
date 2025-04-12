from datetime import datetime
from django.shortcuts import render

# Create your views here.


def home_view(request):
    current_year = datetime.now().year
    return render(request, 'coreapp/index.html',{'current_year':current_year})

def detail_view(request):
    return render(request, 'coreapp/detail.html', {})


def gallery_view(request):
    return render(request, 'coreapp/gallery.html', {})