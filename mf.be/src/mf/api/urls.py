from django.urls import path
from .views import views

urlpatterns = [
    path('products/', views.products),
    path('product/<int:id>/', views.get_product),
    path('product', views.create_product),
    path('tasks/', views.tasks)
]