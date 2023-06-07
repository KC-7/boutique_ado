from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrederLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):  # changed name from vide as duplication of above..
    """ Update order total on lineitem delete """
    instance.order.update_total()
