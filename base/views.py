from django.shortcuts import render
from .models import FgMenuCategory, FgMenuSubCategory, FgMenuItem
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.


def wew(request):

    menu_categories = FgMenuCategory.objects.all

    items_queryset = FgMenuItem.objects.select_related(
        'menu_sub_category__menu_category').filter(menu_sub_category__menu_category_id=1)
    items = serializers.serialize('python', items_queryset)

    categories = FgMenuCategory.objects.filter(id=1).prefetch_related(
        'fgmenusubcategory_set__fgmenuitem_set')
    print(categories)
    coffee = {}
    # for category in categories:
    #     print(f"{category.menu_name}-")
    #     for sub_category in category.fgmenusubcategory_set.all():
    #         print(f"   {sub_category.sub_category_name}:")
    #         for item in sub_category.fgmenuitem_set.all():
    #             print(f"      {item.menu_item_name}")

    for category in categories:
        sub_categories_dict = {}
        for sub_category in category.fgmenusubcategory_set.all():
            menu_items = [
                item.menu_item_name for item in sub_category.fgmenuitem_set.all()]
            sub_categories_dict[sub_category.sub_category_name] = menu_items

        coffee[category.menu_name] = sub_categories_dict
    print(coffee)
    # Printing the coffee dictionary
    # for category, sub_categories in coffee.items():
    #     print(f"{category}:")
    #     for sub_category, menu_items in sub_categories.items():
    #         print(f"   {sub_category}:")
    #         for menu_item in menu_items:
    #             print(f"      {menu_item}")

    icon_classes = {
        'Coffee': 'mug-hot',
        'Lunch': 'burger',
        'Dinner': 'utensils',
        'Dessert': 'ice-cream',
        'Drinks': 'beer-mug-empty',
    }

    context = {
        'items': list(coffee),
        'categories': menu_categories,
        'icon_classes': icon_classes,
    }

    return render(request, 'base/wew.html', context)


def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/about.html')


def reservation(request):
    return render(request, 'base/reservation.html')


def contact(request):
    return render(request, 'base/contact.html')


def menu(request):

    return render(request, 'base/menu.html')
