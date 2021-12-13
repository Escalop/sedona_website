from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 25
    template = 'pages/hotels_list.html'

    class Meta:
        verbose_name = "HoteltList"
        verbose_name_plural = "HotelLists"
        ordering = ('-created_at',)
