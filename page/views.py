from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def introduce(requset):
    return render(requset, 'introduce.html')