from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu_list'),
    path('place_order/', views.place_order, name='place_order'),
     path('enter_name/', views.enter_name, name='enter_name'),  # Name entry form
    path('order_success/', views.order_success, name='order_success'),
]
