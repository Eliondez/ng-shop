from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'main/index.html', {})

def admin(request):
  return render(request, 'main/admin.html', {})