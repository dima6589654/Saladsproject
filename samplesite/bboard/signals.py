from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from bboard.models import Bb


@receiver(post_save, sender=Bb)
def post_save_dispatcher(sender, instance, created, **kwargs):
    if created:
        print(f'Объявление "{instance.title}" создано!')
    else:
        print(f'Объявление "{instance.title}" обновлено!')


add_bb = Signal()


@receiver(add_bb)
def add_bb_dispatcher(sender, instance, **kwargs):
    rubric = instance.rubric
    price = instance.price
    print(f'Объявление в рубрике "{rubric}" с ценой {price:.2f} создано')
