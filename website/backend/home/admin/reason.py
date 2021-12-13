from ..models.home_page import Reasons
from django.contrib import admin



class ReasonInline(admin.TabularInline):
    model = Reasons
    fk_name = 'home_page'
    fields = ('title', 'number','content', 'image')
    extra = 1
