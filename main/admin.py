from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishesAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass