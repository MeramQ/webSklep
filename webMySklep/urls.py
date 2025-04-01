from django.urls import path
from .views import index, admin, add_item, edit_item, delete_item, delete_selected_items

urlpatterns = [
    path('', index, name='index'),
    path('admin-panel/', admin, name='admin-panel'),
    path('admin-panel/add/', add_item, name='add_item'),
    path('admin-panel/edit/<int:item_id>/', edit_item, name='edit_item'),
    path('admin-panel/delete/<int:item_id>/', delete_item, name='delete_item'),
    path('admin-panel/delete-selected/', delete_selected_items, name='delete_selected_items'),
]