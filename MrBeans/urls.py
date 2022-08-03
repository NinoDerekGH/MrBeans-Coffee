from django.urls import path
from . import views

urlpatterns = [
    # ----------Guest Paths----------
    path('', views.home_guest, name="home_guest"),
    path('shop_guest/', views.shop_guest, name="shop_guest"),
    path('faqs_guest/', views.faqs_guest, name="faqs_guest"),
    path('about_guest/', views.about_guest, name="about_guest"),
    path('contact_guest/', views.contact_guest, name="contact_guest"),


    # ----------User Paths----------
    path('home_user/', views.home_user, name="home_user"),
    path('shop_user/', views.shop_user, name="shop_user"),
    path('update_item/', views.updateItem, name="update_item"),
    path('faqs_user/', views.faqs_user, name="faqs_user"),
    path('about_user/', views.about_user, name="about_user"),
    path('contact_user/', views.contact_user, name="contact_user"),


    # ----------Cart, Checkout, Process Order----------
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('process_order/', views.processOrder, name="process_order"),
]