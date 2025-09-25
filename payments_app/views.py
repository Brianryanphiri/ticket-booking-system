from django.shortcuts import render, redirect
from .models import Payment
from tickets_app.models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def payment_page(request):
    if request.method == "POST":
        # For now, simulate payment (later integrate Stripe/PayPal)
        ticket_id = request.POST.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)
        Payment.objects.create(
            user=request.user,
            ticket=ticket,
            amount=ticket.event.price,
            status="pending"
        )
        # Redirect to success for now
        return redirect("payments_app:payment_success")
    tickets = Ticket.objects.filter(user=request.user, payment__isnull=True)
    return render(request, "payments_app/payment_page.html", {"tickets": tickets})

@login_required
def payment_success(request):
    return render(request, "payments_app/payment_success.html")

@login_required
def payment_failed(request):
    return render(request, "payments_app/payment_failed.html")
