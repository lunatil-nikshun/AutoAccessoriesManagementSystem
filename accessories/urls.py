from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_login, name='my_login'),
    path('part_list/', views.part_list, name='part_list'),
    path('part_create/', views.part_create, name='part_create'),
    path('home/', views.home, name='home'),
    path('my_logout/', views.my_logout, name='my_logout'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/accessories/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('search/', views.search_results, name='search_results'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('home_car/', views.search_results_car, name='home_car'),
    path('home_bike/', views.search_results_bike, name='home_bike'),
    path('home_cycle/', views.search_results_cycle, name='home_cycle'),
    path('part_detail/<int:pk>/', views.part_detail, name='part_detail'),
    path('registration/', views.registration, name='registration'),
    path('proceed_to_pay/', views.proceed_to_pay, name='proceed_to_pay'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
]