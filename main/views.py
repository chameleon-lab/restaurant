from django.shortcuts import render
from .models import *

def main_view(request):
    banner = Banner.objects.get(pk=1)

    about = About.objects.get(pk=1)

    special_menu = Dish.objects.filter(category__title='Сезонное меню')

    categories = Category.objects.filter(visible_flag=True)
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.id)

    gallery = Gallery.objects.filter(visible_flag=True)

    contacts = Contacts.objects.get(pk=1)
    schedule = Schedule.objects.all()

    return render(request, 'index.html',
                  context = {'banner': banner, 'about': about, 'special_menu': special_menu, 'categories': categories,
                             'gallery': gallery, 'contacts': contacts, 'schedule': schedule})
