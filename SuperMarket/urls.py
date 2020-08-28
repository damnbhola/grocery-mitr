from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .user import Login

urlpatterns = [
    path('', views.home, name='home'),
    path('login', Login.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
