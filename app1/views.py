from django.shortcuts import render

# Create your views here.
def a(request):
    return render(request,'a.html')
def b(request):
    return render(request,'b.html')