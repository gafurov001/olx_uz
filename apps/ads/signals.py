from django.db.models.signals import post_delete
from django.dispatch import receiver

from ads.models import ProductHistory, Advert


@receiver(post_delete, sender=Advert)
def save_history(instance: Advert, **kwargs):
    if instance:
        ProductHistory.objects.create(product_name=instance.name, product_id=instance.id, price=instance.price)
