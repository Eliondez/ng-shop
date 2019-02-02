from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
  return render(request, 'main/index.html', {})

def add_cat(request):
  return HttpResponse("asdasd")

def admin(request):
  left_buttons = [
    {"name": "Catalog", "href": "catalog", "icon": "fa-tags"},
    {'name': "System", "href": "system", "icon": "fa-cog"}
  ]
  # cats = models.Category.objects.all()
  context = {
    # 'cats': cats,
    "left_buttons": left_buttons
  }
  return render(request, 'main/admin.html', context)