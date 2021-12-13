from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage


class HotelPage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    price = models.IntegerField(verbose_name='Цена', blank=True, null=True)
    type = models.CharField(verbose_name='Тип', max_length=30, blank=True)
    rating_name = models.CharField(verbose_name='Рейтинг', max_length=10, blank=True)
    rating_rate = models.FloatField(blank=True, null=True)
    description = models. CharField(max_length=150, verbose_name='Описание', blank=True)
    image = models.ImageField(blank=True, verbose_name='Изображение')

    template = "pages/hotel.html"

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ("-created_at",)
