from .models import Parents
from django.shortcuts import render

# Create your views here.

def parents(request):
    parents = Parents.objects.all()
    return render(request, 'parents/parents.html', {'parents': parents})
