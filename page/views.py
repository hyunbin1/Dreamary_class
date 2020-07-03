from django.shortcuts import render, get_object_or_404
from .models import Designer
# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(requset, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})
