from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'item-list.html', {'items': items})

def admin(request):
    items = Item.objects.all()
    return render(request, 'admin-panel.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Przedmiot został dodany!")
            return redirect('admin')
    else:
        form = ItemForm()
    return render(request, 'add-item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Przedmiot został zaktualizowany!")
            return redirect('admin')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit-item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, "Przedmiot został usunięty!")
    return redirect('admin')

def delete_selected_items(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        Item.objects.filter(id__in=selected_ids).delete()
        messages.success(request, "Zaznaczone przedmioty zostały usunięte!")
    return redirect('admin')