from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_view, name='create_view'),
    path('', views.list_view, name='list_view'),
    path('<int:id>', views.detail_view, name='detail_view'),
    path('<int:id>/update', views.update_view, name='update_view'),
    path('<int:id>/delete', views.delete_view, name='delete_view'),
]