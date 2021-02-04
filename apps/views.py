from django.shortcuts import render
from .models import ClassProject
# Create your views here.
def index(request):
    return render(request, "index.html")

def createclasspj(request):
    return createclasspj