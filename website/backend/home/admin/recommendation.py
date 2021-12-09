from ..models.home_page import Recommendation
from django.contrib import admin



class RecommendationInline(admin.TabularInline):
    model = Recommendation
    fk_name = 'home_page'
    fields = ('title', 'image', 'content', 'page', 'url')
    extra = 1