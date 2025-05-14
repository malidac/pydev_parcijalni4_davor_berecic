from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket

# Create your views here.
class TicketListView(ListView):
    model = Ticket


class TicketDetailView(DetailView):
    model = Ticket


class TicketCreateView(CreateView):
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets:ticket_list')


class TicketUpdateView(UpdateView):
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets:ticket_list')


class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy('tickets:ticket_list')
