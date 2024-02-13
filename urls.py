from django.urls import path
from . import views
app_name='userapp'
urlpatterns=[
    # path('index',views.index,name=index),
    path('register',views.register),
    path('login',views.login),
    path('main',views.main),
    path('medicines',views.medicines),
    path('details',views.details),
    path('edit',views.edit),
    path('delete',views.delete),
    path('addtocart',views.addtocart),
    path('cart',views.cart),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('product_list',views.product_list,name='product_list'),
    path('cart/',views.view_cart,name='view_cart'),
    # path('', index, name='index'),
    path('search/',views.search,name='search'),
    path('contact/',views.contact,name='contact'),
    path('aboutus',views.aboutus),
    path('payment_page',views.payment_page),
    path('admin_login',views.admin_login),
    path('adminlogin',views.adminlogin),
    path('products',views.products),
    path('productspage',views.productspage),
    path('deleteproduct/<n>',views.deleteproduct),
    path('deleteproductpage',views.deleteproductpage),
    path('../paymentpage', views.paymentpage),
    path('paymentpage', views.paymentpage),
    path('paymentdone',views.payment_page),


    # path('decrease-quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cartItem',views.cartItem),
    path('registerdetails',views.registerdetails),
    path('contactdetails',views.contactdetails),
    path('increment/<int:item_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement/<int:item_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('logout_view',views.logout_view),
    path('',views.index,name='index'),
    path('purchase',views.purchase,name='purchase'),
    path('adminpurchase',views.adminpurchase),



]
