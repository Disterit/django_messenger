from django.urls import path
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)