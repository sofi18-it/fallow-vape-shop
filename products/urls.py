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
]