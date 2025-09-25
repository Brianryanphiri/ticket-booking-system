from django.shortcuts import render, get_object_or_404
from .models import Ticket

# List all tickets
def tickets_list(request):
    """
    Display a list of all tickets.
    """
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, "tickets_app/tickets_list.html", context)

# Show single ticket details
def ticket_detail(request, ticket_id):
    """
    Display detailed information for a single ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    context = {
        "ticket": ticket
    }
    return render(request, "tickets_app/ticket_detail.html", context)
