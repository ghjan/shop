from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    print("product_list 11111,categories:{}, products:{}".format(categories, products))
    if category_slug:
        print("product_list 22222,category_slug:{}".format(category_slug))
        category = get_object_or_404(Category, slug=category_slug)
        print("product_list 33333,category:{}".format(category))
        if category:
            products = products.filter(category=category)
            print("product_list 444444,products:{} after filter for category".format(products))
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
