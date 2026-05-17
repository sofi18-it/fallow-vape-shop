from django.shortcuts import render
from datetime import datetime


def product_detail(request, pk):
    product = {
        "id": pk,
        "title": "Elf Bar BC5000",
        "description": "Популярний одноразовий вейп з ягідним смаком та великою кількістю затяжок."
    }

    related_products = [
        "HQD",
        "Lost Mary",
        "Vuse Go"
    ]

    context = {
        "product": product,
        "related_products": related_products,
        "date": datetime.now()
    }

    return render(request, "detail.html", context)