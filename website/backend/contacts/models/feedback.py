from django.db import models


class Feedback(models.Model):
    email = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Booking(models.Model):
    check_in = models.DateField(verbose_name='ДАТА ЗАЕЗДА')
    check_out = models.DateField(verbose_name='ДАТА ВЫЕЗДА')
    adults = models.IntegerField(verbose_name='ВЗРОСЛЫЕ')
    kids = models.IntegerField(verbose_name='ДЕТИ')
