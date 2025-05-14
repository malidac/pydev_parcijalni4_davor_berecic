from django.urls import path
from .views import (TicketListView,
                    TicketDetailView,
                    TicketCreateView,
                    TicketUpdateView,
                    TicketDeleteView)

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('<int:pk>', TicketDetailView.as_view(), name='ticket_details'),
    path('create', TicketCreateView.as_view(), name='ticket_create'),
    path('update/<int:pk>', TicketUpdateView.as_view(), name='ticket_update'),
    path('delete/<int:pk>', TicketDeleteView.as_view(), name='ticket_delete'),
]