from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ads.models import AdvertisementImage, Advert, FavoriteAdvertisement
from users.models import User


# Register your models here.
@admin.register(AdvertisementImage)
class AdvertisementImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertImageAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteAdvertisement)
class FavoriteAdvertisementAdmin(admin.ModelAdmin):
    pass
