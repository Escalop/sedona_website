from django.db import models


class Booking(models.Model):
    check_in = models.DateField(verbose_name='ДАТА ЗАЕЗДА')
    check_out = models.DateField(verbose_name='ДАТА ВЫЕЗДА')
    adults = models.IntegerField(verbose_name='ВЗРОСЛЫЕ')
    kids = models.IntegerField(verbose_name='ДЕТИ')
    email = models.EmailField(verbose_name='Email', blank=True)

    template = "pages/home.html"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Бронирование гостиницы'
        verbose_name_plural = 'Бронирование гостиниц'

