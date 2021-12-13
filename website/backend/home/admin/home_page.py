from ..models.home_page import HomePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin
from .reason import ReasonInline
from .recommendation import RecommendationInLine


@admin.register(HomePage)
class HomePageAdmin(BasePageAdmin):
    inlines = (ReasonInline,RecommendationInLine)

