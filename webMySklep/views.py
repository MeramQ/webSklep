from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'item-list.html', {'items': items})