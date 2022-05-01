from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def store(request, category_slug=None):
    # add display product by category

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_avaiable=True)
        # add paginator 2
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
# products views
        products = Product.objects.all().filter(is_avaiable=True).order_by('id')
        product_count = products.count()
# add paginator 1
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'product_count' : product_count,
    }
    
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e


    context = {
        'single_product': single_product,
        
    }

    return render(request,'store/product_detail.html',context) 