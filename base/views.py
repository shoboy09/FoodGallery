from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import FgMenuCategory, FgMenuSubCategory, FgMenuItem, Reservation
from .forms import ReserveForm

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

@csrf_protect
def reservation(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reservation = Reservation(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time'],
                guest=form.cleaned_data['guest'],
                message=form.cleaned_data['message']
            )
            reservation.save()
            messages.success(request, 'Reservation submitted successfully!')
            return redirect('reservation')
    else:
        form = ReserveForm()
    
    return render(request, 'base/reservation.html', {'form': form})


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
