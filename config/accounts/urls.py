from django.urls import path, include
from .views import AccountDetailView


urlpatterns = [
    path('<int:pk>/', AccountDetailView.as_view(), name='account_detail')
]
