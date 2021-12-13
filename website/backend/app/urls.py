from django.urls import path, include
from garpixcms.urls import *  # noqa

urlpatterns = [
    path('', include('hotels.urls')),
              ] + urlpatterns  # noqa


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)