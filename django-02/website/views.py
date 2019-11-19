from django.shortcuts import render

# Create your views here.

def mostrarIndex(req):
    return render(req, "index.html")