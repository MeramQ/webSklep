from django.urls import path
from .views import index, admin

urlpatterns = [
    path('', index, name='index'),
    path('admin-panel/', admin, name='admin-panel'),
]