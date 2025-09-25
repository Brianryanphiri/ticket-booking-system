from django.shortcuts import render

# Home page
def home(request):
    return render(request, "events_app/home.html")

# List all events
def events_list(request):
    return render(request, "events_app/events_list.html")
