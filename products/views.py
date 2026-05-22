from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .models import Order


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product, Category
from .forms import ContactForm


class AboutPageView(TemplateView):
    template_name = "about.html"


def product_list(request):
    category_id = request.GET.get("category")

    products = Product.objects.all()
    categories = Category.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "product_list.html", context)


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )


def contact_view(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect("/success/")
    else:
        form = ContactForm()

    return render(
        request,
        "contact.html",
        {"form": form}
    )
@login_required
def profile_view(request):

    return render(
        request,
        "profile.html"
    )
def register_view(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/accounts/login/")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )
@login_required
def dashboard_view(request):

    profile = request.user.profile

    if profile.role != "manager":
        return HttpResponseForbidden(
            "У вас немає доступу"
        )

    products = Product.objects.filter(
        owner=request.user
    )

    orders = Order.objects.filter(
        product__owner=request.user
    )

    context = {
        "products": products,
        "orders": orders
    }

    return render(
        request,
        "dashboard.html",
        context
    )
@api_view(['GET'])
def products_api(request):

    products = Product.objects.all()

    serializer = ProductSerializer(
        products,
        many=True
    )

    return Response(serializer.data)
@login_required
def cart_view(request):

    orders = Order.objects.filter(
        user=request.user
    )

    total = sum(
        order.product.price
        for order in orders
    )

    context = {
        "orders": orders,
        "total": total
    }

    return render(
        request,
        "cart.html",
        context
    )
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    Order.objects.create(
        user=request.user,
        product=product
    )

    return redirect("cart")
@login_required
def remove_from_cart(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order.delete()

    return redirect("cart")

@login_required
def checkout_view(request):

    orders = Order.objects.filter(
        user=request.user
    )

    orders.update(status="processing")

    return render(
        request,
        "success.html"
    )