from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),

    path(
        'product/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'about/',
        views.AboutPageView.as_view(),
        name='about'
    ),

    path(
        'contact/',
        views.contact_view,
        name='contact'
    ),

    path(
        'success/',
        views.AboutPageView.as_view(
            template_name="success.html"
        ),
        name='success'
    ),

    path(
        'profile/',
        views.profile_view,
        name='profile'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),
    path(
    'dashboard/',
    views.dashboard_view,
    name='dashboard'
    ),
    path(
    'api/products/',
    views.products_api,
    name='products_api'
    ),
path(
    'cart/',
    views.cart_view,
    name='cart'
),
path(
    'add-to-cart/<int:product_id>/',
    views.add_to_cart,
    name='add_to_cart'
),
path(
    'remove-from-cart/<int:order_id>/',
    views.remove_from_cart,
    name='remove_from_cart'
),
path(
    'checkout/',
    views.checkout_view,
    name='checkout'
),
]