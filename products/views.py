from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

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
    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        "product_detail.html",
        {"product": product}
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