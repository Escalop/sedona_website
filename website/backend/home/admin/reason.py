from ..models.home_page import Reason
from django.contrib import admin



class ReasonInline(admin.TabularInline):
    model = Reason
    fk_name = 'home_page'
    fields = ('title', 'image', 'number', 'content', 'page', 'url')
    extra = 1
