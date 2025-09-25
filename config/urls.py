from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events_app.urls')),
    path('tickets/', include('tickets_app.urls')),
    path('users/', include('users_app.urls')),
    path('payments/', include('payments_app.urls')),
]
