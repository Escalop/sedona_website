from django.views.generic import ListView
from ..models import Recommendations, Reasons

class ReasonsList(ListView):
    model = Reasons
    query = Reasons.objects.all()
    template_name = 'pages/index.html'
    context_object_name = 'reasons'
    allow_empty = False


class RecommendationsList(ListView):
    model = Recommendations
    query = Recommendations.objects.all()
    template_name = 'pages/index.html'
    context_object_name = 'recommendations'
    allow_empty = False