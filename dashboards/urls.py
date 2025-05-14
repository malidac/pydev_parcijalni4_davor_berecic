from django.urls import path
from .views import DashboardPage

urlpatterns = [
    path('', DashboardPage.as_view(), name='dashboard_page'),
]
