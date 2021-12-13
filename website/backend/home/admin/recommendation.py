from ..models.home_page import Recommendations
from django.contrib import admin



class RecommendationInLine(admin.TabularInline):
    model = Recommendations
    fk_name = 'home_page'
    fields = ('title', 'image', 'content')
    extra = 1
