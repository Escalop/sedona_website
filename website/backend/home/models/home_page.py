from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage
from ..forms.booking import BookingForm
from garpix_notify.models import Notify
from django.conf import settings


class HomePage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    image = models.ImageField(blank=True, upload_to="media/", verbose_name='Изображение')
    template = "pages/index.html"

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save()
                Notify.send(settings.BOOKING_EVENT, {
                    'booking': booking,
                }, email=booking.email)
                context.update({
                    'message': 'Заявка успешно отправлена',
                })
            context.update({
                'form': form,
            })
        return context

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"
        ordering = ("-created_at",)

class Reasons(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    number = models.CharField(max_length=10, verbose_name='Номер')
    content = models.CharField(max_length=250, verbose_name='Cодержание')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, verbose_name='Страница (привязка)', related_name='reason')
    #content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    template = "pages/index.html"

    class Meta:
        verbose_name = "Элемент причина"
        verbose_name_plural = "Элементы причина"


class Recommendations(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    content = models.CharField(max_length=250, verbose_name='Cодержание')
    image = models.FileField(blank=True, verbose_name='Изображение')
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, verbose_name='Страница (привязка)', related_name='recommendation')
    # content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    template = "pages/index.html"

    class Meta:
        verbose_name = "Элемент рекомендация"
        verbose_name_plural = "Элементы рекомендация"






