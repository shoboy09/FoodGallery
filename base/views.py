from django.shortcuts import render, get_object_or_404
from .models import FgMenuCategory, FgMenuSubCategory, FgMenuItem
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.


def wew(request):

    menu_categories = FgMenuCategory.objects.all

    categories = FgMenuCategory.objects.filter(id=1).prefetch_related(
        'fgmenusubcategory_set__fgmenuitem_set')

    icon_classes = {
        'Coffee': 'mug-hot',
        'Lunch': 'burger',
        'Dinner': 'utensils',
        'Dessert': 'ice-cream',
        'Drinks': 'beer-mug-empty',
    }

    context = {
        'items': categories,
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
    menu_categories = FgMenuCategory.objects.all

    categories = FgMenuCategory.objects.filter(id=1).prefetch_related(
        'fgmenusubcategory_set__fgmenuitem_set')

    icon_classes = {
        'Coffee': 'mug-hot',
        'Lunch': 'burger',
        'Dinner': 'utensils',
        'Dessert': 'ice-cream',
        'Drinks': 'beer-mug-empty',
    }

    context = {
        'items': categories,
        'categories': menu_categories,
        'icon_classes': icon_classes,
    }

    return render(request, 'base/wew.html', context)


def getItems(request, category_id):
    category = get_object_or_404(FgMenuCategory, id=category_id)
    items = FgMenuCategory.objects.filter(id=category.id).prefetch_related(
        'fgmenusubcategory_set__fgmenuitem_set')

    category_data = {
        'id': category.id,
        'name': category.menu_name,
        'items': [
            {
                'subcategory': subcategory.sub_category_name,
                'menu_items': [
                    {
                        'name': item.menu_item_name,
                    }
                    for item in subcategory.fgmenuitem_set.all()
                ]
            }
            for subcategory in category.fgmenusubcategory_set.all()
        ]
    }

    return JsonResponse(category_data, safe=False)
