from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('profile/', views.profile, name='profile'),
    path('product/<str:pk>/', views.productview, name='product'),
    path('signup/', views.registerPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('add_product/', views.createProduct, name='add_product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]